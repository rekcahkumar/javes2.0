FROM python:3.8-slim-buster
RUN apt update && apt upgrade -y && \
    apt install --no-install-recommends -y \
        bash \
        curl \
        ffmpeg \
        git \
        libjpeg-dev \
        libjpeg62-turbo-dev \
        libwebp-dev \
        linux-headers-amd64 \
        musl-dev \
        libpq-de \
        python-dev \
        postgresql \
        postgresql-client \
        postgresql-server-dev-all \
        neofetch 
    

RUN git clone https://github.com/rekcahkumar/javes2.0 /root/userbot
RUN mkdir /root/userbot/bin/
WORKDIR /root/userbot/
RUN python3 -m pip install --no-warn-script-location --no-cache-dir --upgrade setuptools wheel -r requirements.txt

ENTRYPOINT ["python", "-m", "userbot"]
