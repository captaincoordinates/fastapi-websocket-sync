import time
from argparse import ArgumentParser
from subprocess import PIPE, Popen

from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer


def generate(search_path: str, output_path: str):
    # execute within new process to avoid module caching
    # caching results in the initial version of the module being used repeatedly
    # https://github.com/phillipdupuis/pydantic-to-typescript/issues/7
    Popen(
        ["python", "-m", "generate", search_path, output_path],
        stdin=PIPE,
        stdout=PIPE,
        stderr=PIPE,
    )


class Event(LoggingEventHandler):
    def __init__(self, search_path: str, output_path: str):
        self.search_path = search_path
        self.output_path = output_path

    def dispatch(self, _):
        generate(self.search_path, self.output_path)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "search_path",
        help="Absolute path of parent directory to all Pydantic type definitions",
        type=str,
        default="/",
    )
    parser.add_argument(
        "output_path",
        help="Absolute path target for generated types",
        type=str,
        default="/tstypes",
    )
    args = vars(parser.parse_args())
    generate(args["search_path"], args["output_path"])
    observer = Observer()
    observer.schedule(
        Event(args["search_path"], args["output_path"]),
        args["search_path"],
        recursive=True,
    )
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
