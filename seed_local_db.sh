# you must have the local postgres instance up and running to call the seed command

docker cp "db_config/northwind_ddl.sql" "fastapi_template-db-1:/tmp"
docker cp "db_config/northwind_data.sql" "fastapi_template-db-1:/tmp"

docker exec fastapi_template-db-1 psql -h localhost -U development_user -d development -a -f /tmp/northwind_ddl.sql
docker exec fastapi_template-db-1 psql -h localhost -U development_user -d development  -a -f /tmp/northwind_data.sql