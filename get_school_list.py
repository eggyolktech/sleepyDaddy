# django shell import
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sleepydaddy.settings")
django.setup()

# imdb process import
from schooltrack.models import School
from bs4 import BeautifulSoup
from decimal import Decimal
import urllib.request
import urllib.parse
import requests
import re
import time
import sys
from datetime import date
from datetime import datetime

def get_school_list_from_kpg():

    url = "http://kgp2016.highlight.hk/web/"

    print("Url: [" + url + "]")
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    
    for link in soup.findAll('a', { "class" : "menubtn_district" }):

        print(link['href'])
        print(link.text.encode("utf-8"))


def main():
    get_school_list_from_kpg()
    
if __name__ == "__main__":
    main()        
        
    

# Send a message to a chat room (chat room ID retrieved from getUpdates)
#send_to_tg_chatroom(passage)

