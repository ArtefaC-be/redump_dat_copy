#!/usr/bin/env python3

import json
import requests
import re
from os.path import isfile, dirname, dirname, abspath
from os import scandir, chdir
from datetime import datetime
from pprint import pprint

import hashlib

class Redump_Dat_Copy:
    def __init__(self):

        _abspath = abspath(__file__)
        _dname = dirname(_abspath)
        chdir(_dname)


        with open('params.json') as f:
            params = json.loads(f.read())
        with open('systems.json','r') as f:
            self.systems = json.loads(f.read())

        self.main_url = params['main_url']
        self.login_url = params['login_url']
        self.timeout = params['timeout']
        self.__username = params['username']
        self.__password = params['password']
        self.destination_path = params['destination_path']

    def run(self):

        summarize = {
            "downloaded": [],
            "error": [],
            "exist": [],
            "unknown": []
        }

        for system in self.systems:
            print(system)
            for item in self.systems[system]:
                full_url = f"{self.main_url}{self.systems[system][item]}"
                print("\t->", item, full_url)
                status_dl = self.download_file(full_url)

                match status_dl[0]:
                    case "error":
                        summarize['error'].append(status_dl[1])
                    case "downloaded":
                        summarize['downloaded'].append(status_dl[1])
                    case "exist":
                        summarize['exist'].append(status_dl[1])
                    case _:
                        summarize['unknown'].append(status_dl[1])

        
        self.calcsha256()
        self.stampdatetime()

        pprint(summarize)

    def download_file(self,url):
            print("Processing:", url)
            with requests.get(url, stream=True, timeout=self.timeout, cookies=self.__cookies) as r:
                try:
                 r.raise_for_status()
                except:
                    print("Erreur")
                    return ["error", url]
                
                try:
                    content_disposition = r.headers['Content-Disposition']
                except:
                    print("An exception occurred")
                    return ["error", url]

                local_filename = re.search(r'".*"', content_disposition).group(0).replace('"','')
                print(f"-> name fetched: {local_filename}")
                # attachment; filename="Acorn - Archimedes - Cuesheets (77) (2025-10-23 18-11-28).zip"

                if isfile(f"{self.destination_path}/{local_filename}"):
                    print("-> The file already exists!")
                    return ["exist", local_filename]

                else:
                    print("-> [DOWNLOADING] The file doesn't exist, let's download!")
                    with open(f"{self.destination_path}/{local_filename}", 'wb') as f:
                        for chunk in r.iter_content(chunk_size=8192): 
                            # If you have chunk encoded response uncomment if
                            # and set chunk_size parameter to None.
                            #if chunk: 
                            f.write(chunk)
                    return ["downloaded", local_filename]


    def login(self):
        with requests.get(self.login_url, timeout=self.timeout) as r:
            cookies = r.cookies
            self.__csrf_token = (re.search(r'<input type="hidden" name="csrf_token" value="(.*?)" />',r.text).group(1))

        data = {
            "req_username": self.__username,
            "req_password": self.__password,
            "form_sent":	"1",
            "redirect_url": "http://forum.redump.org/",
            "csrf_token":	self.__csrf_token,
            "login":	"Login"
        }
        with requests.post(self.login_url, timeout=self.timeout, data=data, cookies=cookies) as r:
            self.__cookies = r.cookies           


    def calcsha256(self):
        print("Compute the SHA256SUM for each files...")
        for file in scandir(self.destination_path):
            if (file.name.endswith('.zip') or file.name.endswith('.dat')) and file.is_file():
                print(f"Processing {file.name}...")
                sha256sum = hashlib.sha256()
                with open(f"{self.destination_path}/{file.name}", 'rb') as source:
                    block = source.read(2**16)
                    while len(block) != 0:
                        sha256sum.update(block)
                        block = source.read(2**16)
                sha256sum_result = sha256sum.hexdigest()
                # Save the sum in .SHA256SUM file.
                with open(f"{self.destination_path}/{file.name}.SHA256SUM", 'w') as f:
                    print(f"{sha256sum_result}\t {file.name}", file=f)
                print('-> SHA256SUM:', sha256sum_result)

    def stampdatetime(self):
        print("Timestamping _last_update.txt...")
        with open(f"{self.destination_path}/_last_update.txt",'w') as f:
            datenow = datetime.now()
            f.write(f"{datenow.strftime('%d/%m/%y %Hh%Mm%Ss')}\n")

def main():
    redump_dat_copy = Redump_Dat_Copy()
    redump_dat_copy.login()
    redump_dat_copy.run()

if __name__ == "__main__":
    main()
