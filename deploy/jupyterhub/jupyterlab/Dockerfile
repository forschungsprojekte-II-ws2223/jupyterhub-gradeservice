FROM jupyter/minimal-notebook:2022-07-06

COPY ./jupyter_notebook_config.py /etc/jupyter/
# Install the libraries specified in the requirements.txt
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
RUN rm requirements.txt

RUN pip install nbgitpuller==1.1.0
RUN jupyter serverextension enable nbgitpuller --sys-prefix