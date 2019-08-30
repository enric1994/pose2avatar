run:
	@docker-compose up -d --build
blender:
	@docker-compose up -d blender
dev-blender:
	@docker exec -it blender bash
pose:
	@docker-compose up -d pose2char
dev-pose:
	@docker exec -it pose2char bash
build:
	@docker-compose build
down:
	@docker-compose down -v
status:
	@docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
logs:
	@docker logs pose2char -f