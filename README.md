# Template FastAPI API

This is a basic starter for FastAPI. It includes a common CORS configuration and request context log middleware, which includes a unique request ID with all log output.

**Note**: If you require DB support check the `db_integration` branch

Exposes a single, simple endpoint at /

Assumes Python 3.9+. Older versions may be compatible but some features require a minimum of 3.8.

## Commands
- `make init`: installs dev dependencies and configures pre-commit formatting and linting hooks
  - installs Python modules, you may wish to establish a virtual environment before running this command
- `make start`: builds and starts API container (http://localhost:8008)
- `make stop`: stops API container
- `make shell`: establishes a terminal within the API container
- `make logs`: tail API container logs
- `make test`: execute API tests in a dedicated container

## Debugging
### Debug API in Visual Studio Code
The following launch.json config can be used to debug the API (http://localhost:8123)
```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "FastAPI",
            "type": "python",
            "request": "launch",
            "module": "app.main",
            "cwd": "${workspaceFolder}",
            "console": "integratedTerminal",
            "justMyCode": false,
            "args":[ "8123" ],
            "env": {
                "API_LOG_LEVEL": "debug"
            }
        }
    ]
}
```
### Debug Tests in Visual Studio Code
- `⌘ + ⇧ + p` to access command prompt and select "Python: Debug All Tests"
- If prompted to "Enable and configure a Test Framework" do this and select pytest
- If prompted to select a root directory choose "."
