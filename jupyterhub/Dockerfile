FROM jupyterhub/jupyterhub:4.0.0

COPY ./jupyterhub_config.py .

RUN pip install --no-cache-dir \
    dockerspawner \
    jupyterhub-idle-culler \
    psycopg2-binary \
    jupyterhub-jwtauthenticator-v2
