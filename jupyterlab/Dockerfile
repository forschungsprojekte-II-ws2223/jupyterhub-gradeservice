FROM jupyter/minimal-notebook:hub-4.0.0

COPY ./jupyter_notebook_config.py /etc/jupyter/
# Install the libraries specified in the requirements.txt
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt --no-cache-dir
RUN rm requirements.txt

RUN jupyter labextension disable "@jupyterlab/apputils-extension:announcements"
