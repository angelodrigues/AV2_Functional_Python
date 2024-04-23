FROM postgres

COPY ./init-scripts/init_table.sql /docker-entrypoint-initdb.d/init_table.sql
COPY ./init-scripts/insert_data.sql /docker-entrypoint-initdb.d/insert_data.sql