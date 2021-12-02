FROM debian:10.11-slim

WORKDIR /ebook_automation

RUN apt-get update && \
    apt-get install -y calibre fontconfig

RUN rm -rf /var/cache/apt/*

COPY run ./

COPY fonts/* /usr/share/fonts/
RUN fc-cache -f -v

ENV OUTDIR=/ebook_automation/output

CMD bash run epub_file
