run:
	@docker-compose up -d --build
pose2avatar:
	@docker-compose up -d pose2avatar
dev-pose2avatar:
	@docker exec -it pose2avatar bash
openpose:
	@docker-compose up -d openpose
dev-openpose:
	@docker exec -it openpose bash
build:
	@docker-compose build
down:
	@docker-compose down -v
status:
	@docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
logs:
	@docker logs pose2avatar -f