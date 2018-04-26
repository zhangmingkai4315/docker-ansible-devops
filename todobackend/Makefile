
# setting default name for project(if not set in env)
PROJECT_NAME ?= todobackend
ORG_NAME ?= mike
REPO_NAME ?= todobackend


# FileName

DEV_COMPOSE_FILE := docker/dev/docker-compose.yml
REL_COMPOSE_FILE := docker/release/docker-compose.yml

REL_PROJECT := $(PROJECT_NAME)$(BUILD_ID)
DEV_PROJECT := $(REL_PROJECT)dev

.PHONY: test build release clean

clean:
	${INFO} "Clean development environment"
	docker-compose -p $(DEV_PROJECT) -f $(DEV_COMPOSE_FILE) kill
	docker-compose -p $(DEV_PROJECT) -f $(DEV_COMPOSE_FILE) rm -f -v

	${INFO} "Clean release environment"
	docker-compose -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) kill
	docker-compose -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) rm -f -v 
	${INFO} "Clean dangling images"
	docker images -q -f dangling=true -f label=application=$(REPO_NAME) | xargs -I ARGS docker rmi -f ARGS
	${INFO} "Clean complete"
test:
	${INFO} "Start test stage"
	docker-compose -p $(DEV_PROJECT) -f $(DEV_COMPOSE_FILE) build
	${INFO} "Components start)"
	docker-compose -p $(DEV_PROJECT) -f $(DEV_COMPOSE_FILE) up agent
	${INFO} "Unit test start"
	docker-compose -p $(DEV_PROJECT) -f $(DEV_COMPOSE_FILE) up test
	${INFO} "Test complete"
build:
	${INFO} "Start build stage"
	docker-compose -p $(DEV_PROJECT) -f $(DEV_COMPOSE_FILE) up builder
	${INFO} "Build complete"
release:
	${INFO} "Start release stage"
	docker-compose -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) build
	${INFO} "Release up agent"
	docker-compose -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) up agent
	${INFO} "Collect static folder for web project"
	docker-compose -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) run --rm app manage.py collectstatic --noinput
	${INFO} "Migrate the database"
	docker-compose -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) run --rm app manage.py migrate --noinput
	${INFO} "Start web serve and do accept test"
	docker-compose -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) up test
	${INFO} "Release complete"


YELLOW := "\e[1;33m"
NC := "\e[0m"
INFO := @bash -c ' \
	printf $(YELLOW); \
	echo "=> $$1" ; \
	printf $(NC)' VALUE