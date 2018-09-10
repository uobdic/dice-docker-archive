DOCKER_IMAGE=kreczko/phedex-site-mon
PORT=5000

build:
	docker build -t ${DOCKER_IMAGE} .

publish:
	docker push ${DOCKER_IMAGE}

run-dev:
	docker run ---name phedex_site_mon -v ${PWD}/webapp:/opt/webapp -p ${PORT}:5000 --rm -ti ${DOCKER_IMAGE}
