build:
	docker build -t remote .
run:
	docker run -it -d -p 8000:8000 --name remote remote
exec:
	docker exec -it remote /bin/bash
start:
	docker start remote
stop:
	docker stop remote
logs:
	docker logs remote
ps:
	docker ps -a
img:
	docker images
rm:
	docker rm -f $$(docker ps -aq)
rmi:
	docker rmi -f $$(docker images -q)
