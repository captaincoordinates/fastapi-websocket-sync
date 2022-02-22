import os
from typing import Final

ENV_VAR_PREFIX: Final = os.environ.get("API_ENV_VAR_PREFIX", "API_")
LOG_LEVEL: Final = os.environ.get(f"{ENV_VAR_PREFIX}LOG_LEVEL", "INFO").upper()
NAME: Final = os.environ.get(f"{ENV_VAR_PREFIX}NAME", "API")
SWAGGER_PATH: Final = os.environ.get(f"{ENV_VAR_PREFIX}SWAGGER_PATH", "/docs")
REDOC_PATH: Final = os.environ.get(f"{ENV_VAR_PREFIX}REDOC_PATH", "/redoc")

CORS_ANY_DOMAIN_REGEX: Final = ".*"
CORS_ANY_LOCALHOST_REGEX: Final = r"http(s)?://localhost(:\d{1,5})?/.*"
