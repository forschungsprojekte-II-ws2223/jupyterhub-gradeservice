FROM jupyter/minimal-notebook:notebook-6.5.2

COPY ./jupyter_notebook_config.py /etc/jupyter/
# Use overrides.json file to change the default settings
RUN mkdir -p ${CONDA_DIR}/share/jupyter/lab/settings
COPY ./overrides.json ${CONDA_DIR}/share/jupyter/lab/settings/overrides.json
# Install the libraries specified in the requirements.txt
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt --no-cache-dir
RUN rm requirements.txt

RUN jupyter serverextension enable nbgitpuller --sys-prefix
