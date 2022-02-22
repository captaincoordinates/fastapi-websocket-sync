TEST_CONTAINER=api_tester
TEST_CONTAINER_IMG=$(TEST_CONTAINER)_img

init:
	pip install -r requirements_dev.txt
	pre-commit install

start:
	docker-compose build
	docker-compose up -d

stop:
	docker-compose down

shell:
	docker-compose exec api /bin/bash

logs:
	docker-compose logs --follow api

test:
	mypy --namespace-packages -p app
	docker-compose build
	docker build -t $(TEST_CONTAINER_IMG) -f app/tests/Dockerfile .
	docker run --rm -v ${PWD}/app/tests:/app/tests $(TEST_CONTAINER_IMG)