NAME = dam-postgresql
RUN = @docker exec -it ${NAME}
RED = \033[0;31m
NC = \033[0m
PSQL = psql -d data -U postgres

db-start:
	@echo "${RED}Starting database...${NC}"
	$(RUN) bash -c "${PSQL}"

show-tables:
	@echo "${RED}Showing tables...${NC}"
	$(RUN) bash -c "${PSQL} -c '\dt'"

select-table:
	@echo "${RED}${table} table:${NC}"
	$(RUN) bash -c "${PSQL} -c 'SELECT * FROM public.${table}'"

describe-table:
	@echo "${RED}Describing ${table} table:${NC}"
	$(RUN) bash -c "${PSQL} -c '\d ${table}'"

flask:
	@echo "${RED}Starting Flask...${NC}"
	docker exec -it dam-backoffice-api bash

docker-reload:
	@echo "${RED}Reloading Docker...${NC}"
	 docker compose down && docker compose up -d --build

docker-rm-all:
	@echo "${RED}Removing all Docker containers...${NC}"
	docker compose down
	docker image rm $$(docker image -a -q)
	docker volume rm $$(docker volume ls -q)
