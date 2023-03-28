TEST_CONTAINER_IMG=api_tester_img

init:
	pip install -r api/requirements_dev.txt
	pre-commit install
	cd web/wss && npm install

start:
	docker compose build
	docker compose up

shell-api:
	docker compose exec api /bin/bash

shell-tsgen:
	docker compose exec tsgenerator /bin/bash

test:
	docker compose build api
	docker build -t $(TEST_CONTAINER_IMG) -f api/app/tests/Dockerfile .
	docker run --rm -v ${PWD}/api/app/tests:/app/tests $(TEST_CONTAINER_IMG)

serve:
	@cd web/wss && ng serve
