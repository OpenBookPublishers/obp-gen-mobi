#!/usr/bin/env python3
from os import path, getenv
from urllib.parse import urljoin
import subprocess
import argparse
from thothlibrary import ThothClient

RUN_PATH = '/ebook_automation/run'
TYPES = {'MOBI', 'AZW3'}

def add_isbn(azw3_path, isbn):
    cmd = f'ebook-meta {azw3_path} --isbn {isbn}'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--doi',
                        help='DOI of the work (registered in Thoth)')
    args = parser.parse_args()

    azw3_path = path.join(getenv('OUT_DIR'), args.doi.split('/')[-1] + '.azw3')
    
    # Execute run.sh
    cmd = f'bash {RUN_PATH} -i file.epub -o {azw3_path}'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    
    doi_url = urljoin('https://doi.org/', args.doi)

    thoth = ThothClient(version="0.8.0")
    query = thoth.query('workByDoi',
                        {'doi': f'"{doi_url}"'})

    for publication in query['publications']:
        if publication['publicationType'] in TYPES:
            add_isbn(azw3_path, publication['isbn'])
            break
    else:
        raise ValueError(f'No {",".join(TYPES)} format(s) defined in Thoth')


if __name__ == '__main__':
    main()
