This folder contains the the docker files and configuration for a deployment of moodle and jupyterhub running behind the traefik reverse proxy.  

The traefik reverse proxy listens on ports 80 and 443 and routes requests to the moodle and jupyterhub servers. It handles issueing and renewing ssl certificates with letsencrypt and automatically forewards http connections to https. More information on traefik can be found [here](https://traefik.io/traefik/).
## setup
- Create proxy network:  
```docker network create proxy```  
- Setup correct ownership and permissions for cert storage file  
```sudo chown root:root ./traefik/data/acme.json && sudo chmod 600 ./traefik/data/acme.json```
- Set the empty environment variables in ```./moodle/.env``` and ```./jupyterhub/.env``` (Make sure to set secure passwords/keys)
- Start the containers:  
```docker compose -f ./traefik/docker-compose.yml up -d```  
```docker compose -f ./jupyterhub/docker-compose.yml up -d```  
```docker compose -f ./moodle/docker-compose.yml up -d```   
- After waiting a bit, you should be able to access the jupyterhub and moodle with the configured adresses
- To check the logs of the containers you can use ```docker logs --follow CONTAINER-NAME```

## references
[traefik & letsencrypt](https://doc.traefik.io/traefik/user-guides/docker-compose/acme-tls/)  
[traefik setup](https://www.dogado.de/vps/vserver-anwendungsfaelle/traefik-reverseproxy-auf-vserver-installieren)  
[moodle setup with traefik](https://www.dogado.de/vps/vserver-anwendungsfaelle/installation-von-moodle)
