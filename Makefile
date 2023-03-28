TEST_CONTAINER=api_tester
TEST_CONTAINER_IMG=$(TEST_CONTAINER)_img

init:
	pip install -r api/requirements_dev.txt
	pre-commit install
	cd web/wss && npm install

start:
	docker compose build
	docker compose up

stop:
	docker compose down

shell-api:
	docker compose exec api /bin/bash

shell-tsgen:
	docker compose exec tsgenerator /bin/bash

logs:
	docker compose logs --follow

test:
	# mypy --namespace-packages -p api
	docker compose build api
	docker build -t $(TEST_CONTAINER_IMG) -f api/app/tests/Dockerfile .
	docker run --rm -v ${PWD}/api/app/tests:/app/tests $(TEST_CONTAINER_IMG)

serve:
	@cd web/wss && ng serve