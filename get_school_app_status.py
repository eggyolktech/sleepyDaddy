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

# django shell import
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sleepydaddy.settings")
django.setup()

from schooltrack.models import School

config = configparser.ConfigParser()
config.read('config.properties')


def get_web_hash_code(url):

    r = requests.get(url)
    #print(r.status_code)
    return hashlib.md5(r.text.encode("utf-8")).hexdigest() 
    
def get_web_last_modified_date(url):

    conn = urllib.request.urlopen(url, timeout=30)
    last_modified = conn.headers['last-modified']
    return last_modified

def main():
    
    school_list = School.objects.filter(is_hot="Y")
    school_list = school_list.exclude(admission_url__isnull=True).exclude(admission_url__exact='')
    
    print("Number of school: " + str(len(school_list)))
    
    for school in school_list:
    
        try:
            name = school.name
            print(name)
        except:
            name = str(school.name.encode("utf-8"))
    
        
        url = school.admission_url
        hash = get_web_hash_code(url)
        
        # if not assign hash yet
        if (not school.admission_url_last_hash):
            school.admission_url_last_hash = hash
            school.admission_url_last_pub_date = datetime.now()
            school.save()
            print(name + " hash created at " + str(school.admission_url_last_pub_date))
        
        # already have case, check if old hash is same as new hash
        else:
            if (not school.admission_url_last_hash == hash):
                school.admission_url_last_hash = hash
                school.admission_url_last_pub_date = datetime.now()
                school.save()
                print(name + " hash updated at " + str(school.admission_url_last_pub_date))
            else:
                print(name + " hash has no change.")
                
    #print(get_web_hash_code('http://playgroup.msc.edu.hk/index.php/zh/application-c'))
    #print(get_web_last_modified_date('http://playgroup.msc.edu.hk/index.php/zh/application-c'))
    
    #print(get_web_hash_code('http://stock.eggyolk.tech/aa.html'))
    #print(get_web_last_modified_date('http://stock.eggyolk.tech/'))
    
    
if __name__ == "__main__":
    main()        
        

