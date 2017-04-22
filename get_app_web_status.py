from bs4 import BeautifulSoup
from decimal import Decimal
import urllib.request
import urllib.parse
import hashlib
import requests
import re
from datetime import date
from datetime import datetime
import configparser

config = configparser.ConfigParser()
config.read('config.properties')


def get_web_hash_code(url):

    r = requests.get(url)
    print(r.status_code)
    return hashlib.md5(r.text.encode("utf-8")).hexdigest() 
    
def get_web_last_modified_date(url):

    conn = urllib.request.urlopen(url, timeout=30)
    last_modified = conn.headers['last-modified']
    return last_modified

def main():
    print(get_web_hash_code('http://playgroup.msc.edu.hk/index.php/zh/application-c'))
    print(get_web_last_modified_date('http://playgroup.msc.edu.hk/index.php/zh/application-c'))
    
    print(get_web_hash_code('http://stock.eggyolk.tech/aa.html'))
    print(get_web_last_modified_date('http://stock.eggyolk.tech/'))
    
    
if __name__ == "__main__":
    main()        
        

