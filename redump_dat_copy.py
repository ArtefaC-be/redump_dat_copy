#!/usr/bin/env python3

import requests
import re
from os.path import isfile
from os import scandir
import hashlib
import argparse
from datetime import datetime
from urllib.parse import unquote


MAIN_URL = "https://old.redump.info"
TIMEOUT=120

DESTINATION_PATH = "./files"



class Redump_Dat_Copy:
    def ___init__(self):
        pass

    def full(self):
        print("Full operation...")
        self.get_source_page()
        urls = self.extract_url()
        final_urls = self.get_moved_http_request(urls)
        self.download_files(final_urls)
        self.calcsha256()
        self.stampdatetime()

    def get_source_page(self):
        # Get the source page and write into source.text
        print(f"Fetch the page source ({MAIN_URL})")
        with requests.Session() as s:
            s.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:144.0) Gecko/20100101 Firefox/144.0"}
            r = s.get(f"{MAIN_URL}/downloads",timeout=TIMEOUT)
        with open("source.text",'w') as f:
            f.write(r.text)

    def extract_url(self):
        content = None
        with open("source.text", 'r') as f:
            content = f.read()

        # Get the table that contains all the url
        main_table = re.search(r'<table .*</table>',content,flags=re.DOTALL).group(0)

        # Search all the link in the table
        pattern = re.compile(r'/[a-z]+\/[a-z-]+/')
        pathes = pattern.findall(main_table)
        urls = []
        for path in pathes:
            urls.append(f"{MAIN_URL}{path}")

        # Print finded urls
        for url in urls:
            print(url)
        return urls

    def get_moved_http_request(self,urls):

        newlocation = []
        for url in urls:
            with requests.Session() as s:
                s.headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:144.0) Gecko/20100101 Firefox/144.0"}
                r = s.get(url,allow_redirects=False)
                newlocation.append(f"{MAIN_URL}/{r.headers['Location']}")

        return newlocation


    def download_files(self,urls):
        for url in urls:
            local_filename = url.split('/')[-1]
            local_filename = unquote(local_filename)
            print(local_filename)
            if isfile(f"{DESTINATION_PATH}/{local_filename}"):
                print("-> Already exists!")
                continue

            else:
                print("-> [DOWNLOADING] Doesn't exist!")
                # NOTE the stream=True parameter below
                with requests.get(url, stream=True) as r:
                    r.raise_for_status()
                    with open(f"{DESTINATION_PATH}/{local_filename}", 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192): 
                            f.write(chunk)

    def calcsha256(self):
        print("Compute the SHA256SUM for each files...")
        for file in scandir(DESTINATION_PATH):
            if (file.name.endswith('.zip') or file.name.endswith('.dat')) and file.is_file():
                print(f"Processing {file.name}...")
                sha256sum = hashlib.sha256()
                with open(f"{DESTINATION_PATH}/{file.name}", 'rb') as source:
                    block = source.read(2**16)
                    while len(block) != 0:
                        sha256sum.update(block)
                        block = source.read(2**16)
                sha256sum_result = sha256sum.hexdigest()
                # Save the sum in .SHA256SUM file.
                with open(f"{DESTINATION_PATH}/{file.name}.SHA256SUM", 'w') as f:
                    print(f"{sha256sum_result}\t {file.name}", file=f)
                print('-> SHA256SUM:', sha256sum_result)

    def stampdatetime(self):
        print("Timestamping last_update.txt...")
        with open(f"{DESTINATION_PATH}/last_update.txt",'w') as f:
            datenow = datetime.now()
            f.write(f"{datenow.strftime('%d/%m/%y %Hh%Mm%Ss')}\n")
    

def main():
    parser = argparse.ArgumentParser(
                    prog='redump_dat_copy.py',
                    description='This program fetch all the data files from old.redump.info.',
                    epilog='Created by ArtefaC')

    parser.add_argument('function', default='all', help="can be 'all' 'source' 'url' 'download' 'calcsum' 'stamp'")
    args = parser.parse_args()

    redump_dat_copy = Redump_Dat_Copy()

    match args.function:
        case "all":
            redump_dat_copy.full()
        case "source":
            redump_dat_copy.get_source_page()
        case "url":
            redump_dat_copy.extract_url()
        case "download":
            urls = redump_dat_copy.extract_url()
            final_urls = redump_dat_copy.get_moved_http_request(urls)
            redump_dat_copy.download_files(final_urls)
        case "calcsum":
            redump_dat_copy.calcsha256()
        case "stamp":
            redump_dat_copy.stampdatetime()

if __name__ == "__main__":
    main()

