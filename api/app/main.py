from logging import getLogger
from typing import Final

from app import settings
from app.middleware.request_context_log_middleware import RequestContextLogMiddleware
from app.routes import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

LOGGER: Final = getLogger(__file__)


app = FastAPI(
    title=settings.NAME,
    docs_url=settings.SWAGGER_PATH,
    redoc_url=settings.REDOC_PATH,
)
app.include_router(router)

# CORS configuration, select appropriate CORS regex from settings
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=settings.CORS_ANY_LOCALHOST_REGEX,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Log messages with unique request IDs
app.add_middleware(RequestContextLogMiddleware)


# Development / debug support, not executed when running in container
# Start a local server on port 8008 by default,
# or whichever port was provided by the caller, when script / module executed directly
if __name__ == "__main__":
    import sys

    import uvicorn  # type: ignore

    port = 8008 if len(sys.argv) == 1 else int(sys.argv[1])
    LOGGER.info("Available on port %d", port)
    LOGGER.debug("Debug logging enabled if visible")
    uvicorn.run(app, host="0.0.0.0", port=port)
