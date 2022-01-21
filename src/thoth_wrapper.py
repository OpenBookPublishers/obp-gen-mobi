#!/usr/bin/env python3
from os import path
from urllib.parse import urljoin
import subprocess
import argparse
from thothlibrary import ThothClient

RUN_PATH = '/ebook_automation/run'
AZW3_PATH = '/ebook_automation/output/file.azw3'
TYPES = {'MOBI', 'AZW3'}

def add_isbn(isbn):
    cmd = f'ebook-meta {AZW3_PATH} --isbn {isbn}'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--doi',
                        help='DOI of the work (registered in Thoth)')
    args = parser.parse_args()

    # Execute run.sh
    cmd = f'bash {RUN_PATH} file'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    
    doi_url = urljoin('https://doi.org/', args.doi)

    thoth = ThothClient(version="0.6.0")
    query = thoth.query('workByDoi',
                        {'doi': f'"{doi_url}"'})

    for publication in query['publications']:
        if publication['publicationType'] in TYPES:
            add_isbn(publication['isbn'])
            break
    else:
        raise ValueError(f'No {",".join(TYPES)} format(s) defined in Thoth')


if __name__ == '__main__':
    main()
