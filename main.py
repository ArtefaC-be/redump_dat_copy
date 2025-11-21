#!/usr/bin/env python3
from redump_web import Redump_Dat_Copy
import argparse




def main():
    parser = argparse.ArgumentParser(
                    prog='redump_dat_copy.py',
                    description='This program fetch all the data files from redump.org.',
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

