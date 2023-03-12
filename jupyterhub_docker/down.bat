docker compose down -v

docker volume rm $(docker volume ls -f name=jupyterhub-user -q)
