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

    print("Base Url: [" + url + "]")
    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    r = requests.get(url, headers=headers)
    html = r.text
    soup = BeautifulSoup(html, "html.parser")
    
    for link in soup.findAll('a', { "class" : "menubtn_district" }):

        suburl = url + link['href']
                
        print(suburl)
        
        subr = requests.get(suburl, headers=headers)
        subhtml = subr.text
        subsoup = BeautifulSoup(subhtml, "html.parser")
        
        _district = suburl.split("=")[-1]
        
        print("District: [" + _district + "]")
        
        for table in subsoup.findAll('table', { "class" : "font_content_school_list" }):
        
            #if (not _district == "shatin"):
            #    continue
        
            td = table.findAll('td')[0]            
            _schid = re.findall('\d+', td['onclick'])[0]
            
            schurl = 'http://kgp2016.highlight.hk/web/schoolinfo.php?schid=' + _schid
            print("School URL: [" + schurl + "]")
            
            response = urllib.request.urlopen(schurl)
            schhtml = response.read().decode("utf-8")   
            schsoup = BeautifulSoup(schhtml, "html5lib")
            
            if (not schsoup.findAll('table', { "class" : "font_content_schoolinfo"})):
                print("School HTML: [" + schhtml + "]")
                
            headtable = schsoup.findAll('table', { "class" : "font_content_schoolinfo"})[0]
            
            infotables = schsoup.findAll('table', { "class" : "font_content_box" })
            highlighttable = schsoup.findAll('table', { "class" : "Font_District_Name"})[0]
            
            _name = headtable.findAll('tr')[0].text.strip()
            _address = headtable.findAll('tr')[2].findAll('td')[1].text.strip()
            _phone_no = headtable.findAll('tr')[4].findAll('td')[1].text.strip()
            _fax_no = headtable.findAll('tr')[6].findAll('td')[1].text.strip()
            
            _school_no = infotables[0].findAll('td')[1].text
            _location_no = infotables[1].findAll('td')[1].text
            _school_year = infotables[2].findAll('td')[0].text
            
            if (infotables[2].findAll('td')[3].text.strip() == "有"):
                _voucher = "Y"
            else:
                _voucher = "N"
            
            _school_cat = infotables[3].findAll('td')[1].text
            _student_type = infotables[3].findAll('td')[3].text
            
            if (infotables[3].findAll('a') and not "Not Available" in infotables[3].findAll('a')[0].text):
                _school_url = infotables[3].findAll('a')[0].text
            else:
                _school_url = ""
            
            _highlight_url = url + highlighttable.findAll('a')[0]['href']
            
            if (_school_cat.strip() == "私立獨立"):
                _category = "PI"
            else:
                _category = "NPM"
                
            if (_student_type.strip() == "男女"):
                _student_category = "COED"
            else:
                _student_category = "SINS"

            
            _tpratio_am = infotables[6].findAll('td')[1].text.strip()
            _tpratio_pm = infotables[6].findAll('td')[3].text.strip()
            
            _rows = infotables[7].findAll('tr')
            _vacancy_n_list = [_rows[1].findAll('td')[1].text.strip(), _rows[2].findAll('td')[1].text.strip(), _rows[3].findAll('td')[1].text.strip()] 
            _vacancy_lkg_list = [_rows[1].findAll('td')[2].text.strip(), _rows[2].findAll('td')[2].text.strip(), _rows[3].findAll('td')[2].text.strip()]
            _vacancy_ukg_list = [_rows[1].findAll('td')[3].text.strip(), _rows[2].findAll('td')[3].text.strip(), _rows[3].findAll('td')[3].text.strip()]
            #_vacancy_pn_list = [_rows[1].findAll('td')[2].text, _rows[2].findAll('td')[].text, _rows[3].findAll('td')[1].text]
            
            _rows = infotables[8].findAll('tr')
            
            try:
                _annual_fee_n_list = [_rows[1].findAll('td')[2].text.strip(), _rows[2].findAll('td')[1].text.strip(), _rows[3].findAll('td')[1].text.strip()]                
                _annual_fee_lkg_list = [_rows[1].findAll('td')[3].text.strip(), _rows[2].findAll('td')[2].text.strip(), _rows[3].findAll('td')[2].text.strip()]
                _annual_fee_ukg_list = [_rows[1].findAll('td')[4].text.strip(), _rows[2].findAll('td')[3].text.strip(), _rows[3].findAll('td')[3].text.strip()]
            except Exception as e:
                _annual_fee_n_list = ["-", "-", "-"]
                _annual_fee_lkg_list = ["-", "-", "-"]
                _annual_fee_ukg_list = ["-", "-", "-"]
            
            _rows = infotables[10].findAll('tr')
            _annual_fee_pn_list = [_rows[2].findAll('td')[0].text.strip(), _rows[2].findAll('td')[1].text.strip()]
            _vacancy_pn_list = [_rows[4].findAll('td')[1].text.strip()]
            
            
            if (infotables[11].findAll('tr')[1].findAll('td')[1].text.strip() == "本地"):
                _curriculum = "LOCAL"
            else:
                _curriculum = "NLOCAL"
           
            _kgp_url = schurl
            
            # new school needs to be created            
            s = School(school_no=_school_no, location_no=_location_no, district=_district, school_year=_school_year, name=_name.encode("utf-8"), address=_address.encode("utf-8"), phone_no=_phone_no, fax_no=_fax_no, voucher=_voucher, category=_category, student_category=_student_category, school_url=_school_url, highlight_url=_highlight_url, tpratio_am=_tpratio_am, tpratio_pm=_tpratio_pm, vacancy_pn_list=_vacancy_pn_list, vacancy_n_list=_vacancy_n_list, vacancy_lkg_list=_vacancy_lkg_list, vacancy_ukg_list=_vacancy_ukg_list, annual_fee_pn_list=_annual_fee_pn_list, annual_fee_n_list=_annual_fee_n_list, annual_fee_lkg_list=_annual_fee_lkg_list, annual_fee_ukg_list=_annual_fee_ukg_list, curriculum=_curriculum, kgp_url=_kgp_url)
            s.save()   
            
        
def main():
    get_school_list_from_kpg()
    
if __name__ == "__main__":
    main()        
        
    

# Send a message to a chat room (chat room ID retrieved from getUpdates)
#send_to_tg_chatroom(passage)

