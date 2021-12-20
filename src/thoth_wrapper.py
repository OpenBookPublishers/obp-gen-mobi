#!/usr/bin/env python3
from os import path
from urllib.parse import urljoin
import subprocess
import argparse
from thothlibrary import ThothClient

RUN_PATH = '/ebook_automation/run'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--doi',
                        help='DOI of the work (registered in Thoth)')
    args = parser.parse_args()

    # Execute run.sh
    cmd = f'bash {RUN_PATH} epub_file'
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    stdout, stderr = p.communicate()
    
#    doi_url = urljoin('https://doi.org/', args.doi)

#    thoth = ThothClient(version="0.6.0")
#    query = thoth.query('workByDoi',
#                        {'doi': f'"{doi_url}"'})


if __name__ == '__main__':
    main()
