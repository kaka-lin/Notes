include .env

notebook_image:
	docker build -t $(LOCAL_NOTEBOOK_IMAGE) \
		--build-arg JUPYTERHUB_VERSION=$(USER_JUPYTERHUB_VERSION) \
		singleuser

build:
	docker-compose build

clean:

.PNONY: clean
