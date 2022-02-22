from argparse import ArgumentParser
from glob import glob
from importlib import import_module
from inspect import isclass
from os import path
from re import escape, sub
from sys import path as syspath

from pydantic import BaseModel
from pydantic2ts import generate_typescript_defs

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "search_path",
        type=str,
    )
    parser.add_argument(
        "output_path",
        type=str,
    )
    args = vars(parser.parse_args())
    for file_path in [
        filename
        for filename in glob(path.join(args["search_path"], "**", "*.py"), recursive=True)
        if filename != "__init__.py"
    ]:
        module_path = path.dirname(file_path)
        relative_module_path = module_path.replace(args["search_path"], "")
        module_name = path.basename(file_path)[:-3]
        path_parts = [
            part
            for part in [
                sub(rf"^{escape(path.sep)}", "", relative_module_path),
                module_name,
            ]
            if part
        ]
        module_str = f"{path.sep.join(path_parts).replace(path.sep, '.')}"
        if module_path not in syspath:
            syspath.append(args["search_path"])
        try:
            module = import_module(module_str)
        except ImportError as e:
            raise Exception(
                f"unable to import type class from module '{module_str}': {e}"
            )

        types = [
            type_class
            for type_class in module.__dict__.values()
            if isclass(type_class)
            and type_class is not BaseModel
            and issubclass(type_class, BaseModel)
        ]

        ts_path = path.join(args["output_path"], f"api_{module_name}.ts")
        print(f"generating TypeScript type for {module_str} to {ts_path}")
        generate_typescript_defs(module_str, ts_path)
