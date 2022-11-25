FROM jupyterhub/jupyterhub:2.3.1

COPY ./jupyterhub_config.py .

RUN pip install --no-cache-dir \
    dockerspawner==12.1.0 \
    jupyterhub-idle-culler==1.2.1 \
    psycopg2-binary==2.9.3 \
    jupyterhub-jwtauthenticator-v2==2.0.3