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
	$(RUN) bash -c "${PSQL} -c 'SELECT * FROM ${table}'"

describe-table:
	@echo "${RED}Describing ${table} table:${NC}"
	$(RUN) bash -c "${PSQL} -c '\d ${table}'"

recreate-app:
	@echo "${RED}Recreating app...${NC}"
	$(RUN) docker compose down
