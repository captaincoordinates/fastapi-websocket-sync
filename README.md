# FastAPI Websocket Sync

Prototyping cross-process websocket communication in FastAPI.

FastAPI running in Gunicorn or Uvicorn sometimes runs with more than one worker process. When an API works exclusively with stateless, atomic request / response exchanges this is not a problem and it is fine for any number of processes to run in isolation. Each request issued by a client could be serviced by a different worker process transparently without a problem.

A websocket is a persistent connection between the client and API. Any communication over the websocket is managed by the worker process that first established the connection. If logic within the API wants to broadcast a message to websocket clients it is constrained by its worker process and only able to send messages to the clients whose connection the process is managing. This results in some clients not receiving some messages.

The goal of this repo is to demonstrate a mechanism to push messages to all websocket clients across all worker processes. The plan is to use [FastAPI Events](https://github.com/melvinkcx/fastapi-events/) to dispatch messages - from the worker process that needs to communicate with all websocket clients - to a queueing mechanism hosted by the API container such as ZeroMQ or RabbitMQ. All worker processes will listen for messages in that queue. If PID 1 dispatches a message to ZeroMQ via FastAPI Events then PIDs 1, 2, and 3 should receive that message and push to their websocket clients.

This prototype aims to support cross-process communication within a single container, but the same technique could be used with an external queueing mechanism, such as AWS SQS, to communicate across multiple containers. The goal of this prototype is to eventually demonstrate this configuration, but initially it is only concerned with the single container scenario.

This repo also demonstrates Pydantic-to-TypeScript type conversion, provided by [this repo](https://github.com/captaincoordinates/pydantic-typescript-sync), which ensures client TypeScript logic references the same types as server Python logic.

Assumes Python 3.9+. Other versions may be compatible but some features require a minimum of 3.8. Requires a Node environment for `make serve`.

## Commands
- `make init`: installs dev dependencies and configures pre-commit formatting and linting hooks
- `make start`: builds and starts containers. API available at http://localhost:8008
    - does not currently support hot-reloading in combination with >1 worker process. API container should be stopped/started to acknowledge code changes (it does not need to be rebuilt)
- `make serve`: starts the Angular development server, which includes a watch-build and supports hot-reload, so Angular changes should immediately be reflected at http://localhost:4200
    - kill with Ctrl+C. UI requires running API container from `make start`
- `make shell-api`: establishes a terminal within the API container
- `make shell-tsgen`: establishes a terminal within the tsgenerator container
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
            "cwd": "${workspaceFolder}/api",
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
