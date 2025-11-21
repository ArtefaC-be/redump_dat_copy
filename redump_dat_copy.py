#!/usr/bin/env python3

import json
from pprint import pprint

class Redump_Dat_Copy:
    def __init__(self):
        with open('params.json') as f:
            params = json.loads(f.read())
        with open('systems.json','r') as f:
            self.systems = json.loads(f.read())

        self.main_url = params['main_url']
        pprint(self.systems)        
        self.run()

    def run(self):
        for system in self.systems:
            print(system)
            for item in self.systems[system]:
                print("->", item)
                print("->", f"{self.main_url}{self.systems[system][item]}")






def main():
    print("Hello world")

    redump_dat_copy = Redump_Dat_Copy()

if __name__ == "__main__":
    main()

