#!/usr/bin/env python3

import requests
import re
from os.path import isfile
from os import scandir
import hashlib
import argparse
from datetime import datetime
from urllib.parse import unquote


MAIN_URL = "http://redump.org"
TIMEOUT=120

DESTINATION_PATH = "./files"



class Redump_Dat_Copy:
    def ___init__(self):
        pass

    def full(self):
        print("Full operation...")
        self.download_files()
        self.calcsha256()
        self.stampdatetime()


    def download_files(self):
        with open('urls.txt','r') as f:
            urls = [line.strip() for line in f]

        for url in urls:
            print("Processing:", url)
            with requests.get(url, stream=True, timeout=TIMEOUT) as r:
                r.raise_for_status()

                content_disposition = r.headers['Content-Disposition']
                local_filename = re.search(r'".*"', content_disposition).group(0).replace('"','')
                print(f"-> name fetched: {local_filename}")
                # attachment; filename="Acorn - Archimedes - Cuesheets (77) (2025-10-23 18-11-28).zip"

                if isfile(f"{DESTINATION_PATH}/{local_filename}"):
                    print("-> The file already exists!")

                else:
                    print("-> [DOWNLOADING] The file doesn't exist, let's download!")
                    with open(f"{DESTINATION_PATH}/{local_filename}", 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192): 
                            # If you have chunk encoded response uncomment if
                            # and set chunk_size parameter to None.
                            #if chunk: 
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

    parser.add_argument('function', default='all', help="can be 'all' 'download' 'calcsum' 'stamp'")
    args = parser.parse_args()

    redump_dat_copy = Redump_Dat_Copy()

    match args.function:
        case "all":
            redump_dat_copy.full()
        case "download":
            redump_dat_copy.download_files()
        case "calcsum":
            redump_dat_copy.calcsha256()
        case "stamp":
            redump_dat_copy.stampdatetime()

if __name__ == "__main__":
    main()

