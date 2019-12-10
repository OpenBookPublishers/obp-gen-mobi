FROM python:3.8.0-slim-buster

WORKDIR /ebook_automation

RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

RUN apt-get update && \
    apt-get install -y wget tar xz-utils xdg-utils

RUN rm -rf /var/cache/apt/*

RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

COPY run ./

CMD bash run epub_file
