# Removes jupyterhub and jupyterhub-db containers and volumes
docker compose down -v

# Removes user volumes
docker volume rm $(docker volume ls -f name=jupyterhub-user -q)
