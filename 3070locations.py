import os
from re import compile
from re import match
import rtxscraper
from datetime import datetime

def narrow_search():
    if os.path.exists("rtx3070-Stock.txt"):
        f = open("rtx3070-Stock.txt", "r")
    info = f.read()
    f.close()

    HamRE = '.*Hamilton.*'
    MissRE = '.*Mississauga.*'
    EtobRE = '.*Etobicoke.*'
    WlooRE = '.*Waterloo.*'
    BurlRE = '.*Burlington.*'
    STCathRE = '.*St. Catharines.*'

    non_zero = '.* : [0-9].*'
    non_zero_pattern = compile(non_zero)

    Ham_pattern = compile(HamRE)
    Miss_pattern = compile(MissRE)
    Etob_pattern = compile(EtobRE)
    Wloo_pattern = compile(WlooRE)
    Burl_pattern = compile(BurlRE)
    STCath_pattern = compile(STCathRE)

    results = []
    for lines in info.split('\n'):
        if Ham_pattern.match(lines) and non_zero_pattern.match(lines):
            results.append(lines)

        if Burl_pattern.match(lines) and non_zero_pattern.match(lines):
            results.append(lines)

        if STCath_pattern.match(lines) and non_zero_pattern.match(lines):
            results.append(lines)

        if Miss_pattern.match(lines) and non_zero_pattern.match(lines):
            results.append(lines)

        if Etob_pattern.match(lines) and non_zero_pattern.match(lines):
            results.append(lines)

        if Wloo_pattern.match(lines) and non_zero_pattern.match(lines):
            results.append(lines)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")      
    if os.path.exists("rtx3070.txt"):
            os.remove("rtx3070.txt")
    f = open("rtx3070.txt", "w")
    f.write(current_time + '\n')
    for line in results:
        f.write(line + '\n')
    f.close()

if __name__ == '__main__':
    rtxscraper.all_locations()
    narrow_search()