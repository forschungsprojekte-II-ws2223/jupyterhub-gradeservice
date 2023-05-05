FROM python:3.11-slim

RUN apt update && apt install -y \
    curl \
    ca-certificates \
    gpg \
    pandoc \
    texlive-xetex \
    texlive-fonts-recommended \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Install docker cli
RUN install -m 0755 -d /etc/apt/keyrings
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
RUN chmod a+r /etc/apt/keyrings/docker.gpg
RUN echo \
    "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
    "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
    tee /etc/apt/sources.list.d/docker.list > /dev/null

RUN apt update && apt install --no-install-recommends -y \
    docker-ce-cli \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

# Install gradeservice
WORKDIR /app

COPY . .

RUN pip install .
CMD ["/bin/bash", "-c", "uvicorn gradeservice.main:app --reload --host 0.0.0.0 --port 5000"]
