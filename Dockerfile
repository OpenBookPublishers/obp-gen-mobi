FROM python:3.8.0-slim-buster

WORKDIR /ebook_automation

RUN apt-get update && \
    apt-get install -y calibre fontconfig

RUN rm -rf /var/cache/apt/*

COPY run ./
COPY src/thoth_wrapper.py ./

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN rm requirements.txt

COPY fonts/* /usr/share/fonts/
RUN fc-cache -f -v

ENV OUTDIR=/ebook_automation/output

ENTRYPOINT ["python3"]

CMD ["thoth_wrapper.py", "--help"]
