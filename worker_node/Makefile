
build: build-centos7 build-centos6

build-centos6:
	docker build -t kreczko/workernode6 -f centos6/Dockerfile .

build-centos7:
	docker build -t kreczko/workernode7 -f centos7/Dockerfile .

publish: publish-centos7 publish-centos6

publish-centos7:
	docker push kreczko/workernode7

publish-centos6:
	docker push kreczko/workernode6
