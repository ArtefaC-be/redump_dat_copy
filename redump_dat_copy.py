#!/usr/bin/env python3

import json
from pprint import pprint
import requests
import re
from os.path import isfile
from os import scandir

import hashlib

class Redump_Dat_Copy:
    def __init__(self):
        with open('params.json') as f:
            params = json.loads(f.read())
        with open('systems.json','r') as f:
            self.systems = json.loads(f.read())

        self.main_url = params['main_url']
        self.timeout = params['timeout']
        self.detination_path = params['destination_path']
        self.run()

    def run(self):
        for system in self.systems:
            print(system)
            for item in self.systems[system]:
                full_url = f"{self.main_url}{self.systems[system][item]}"
                print("\t->", item, full_url)
                self.download_file(full_url)
        
        self.calcsha256()

    def download_file(self,url):
            print("Processing:", url)
            with requests.get(url, stream=True, timeout=self.timeout) as r:
                try:
                 r.raise_for_status()
                except:
                    print("Erreur")
                    return
                
                try:
                    content_disposition = r.headers['Content-Disposition']
                except:
                    print("An exception occurred")
                    return

                local_filename = re.search(r'".*"', content_disposition).group(0).replace('"','')
                print(f"-> name fetched: {local_filename}")
                # attachment; filename="Acorn - Archimedes - Cuesheets (77) (2025-10-23 18-11-28).zip"

                if isfile(f"{self.detination_path}/{local_filename}"):
                    print("-> The file already exists!")

                else:
                    print("-> [DOWNLOADING] The file doesn't exist, let's download!")
                    with open(f"{self.detination_path}/{local_filename}", 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192): 
                            # If you have chunk encoded response uncomment if
                            # and set chunk_size parameter to None.
                            #if chunk: 
                            f.write(chunk)

    def calcsha256(self):
        print("Compute the SHA256SUM for each files...")
        for file in scandir(self.detination_path):
            if (file.name.endswith('.zip') or file.name.endswith('.dat')) and file.is_file():
                print(f"Processing {file.name}...")
                sha256sum = hashlib.sha256()
                with open(f"{self.detination_path}/{file.name}", 'rb') as source:
                    block = source.read(2**16)
                    while len(block) != 0:
                        sha256sum.update(block)
                        block = source.read(2**16)
                sha256sum_result = sha256sum.hexdigest()
                # Save the sum in .SHA256SUM file.
                with open(f"{DESTINATION_PATH}/{file.name}.SHA256SUM", 'w') as f:
                    print(f"{sha256sum_result}\t {file.name}", file=f)
                print('-> SHA256SUM:', sha256sum_result)

def main():

    redump_dat_copy = Redump_Dat_Copy()

if __name__ == "__main__":
    main()

