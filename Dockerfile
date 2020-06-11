FROM python:3.8.0-slim-buster

WORKDIR /ebook_automation

RUN apt-get update && \
    apt-get install -y wget tar xz-utils xdg-utils fontconfig

RUN rm -rf /var/cache/apt/*

RUN wget -nv -O- https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

COPY run ./

COPY fonts/* /usr/share/fonts/
RUN fc-cache -f -v

ENV OUTDIR=/ebook_automation/output

CMD bash run epub_file
