from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from datetime import datetime
from datetime import date
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your models here.
class School(models.Model):
    school_no = models.CharField(max_length=8)
    location_no = models.CharField(max_length=20) 
    
    DISTRICT = (
        ('central', '中西區'),
        ('hkeast', '港島東區'),
        ('islands', '離島區'),
        ('southern', '南區'),
        ('wanchai', '灣仔區'),
        ('kwaichung', '葵青區'),
        ('tsuenwan', '荃灣區'),
        ('tuenmun', '屯門區'),
        ('yuenlong', '元朗區'),
        ('north', '北區'),
        ('shatin', '沙田區'),
        ('taipo', '大埔區'),
        ('kowlooncity', '九龍城區'),
        ('kwuntong', '觀塘區'),
        ('saikung', '西貢區'),
        ('shamshuipo', '深水埗區'),
        ('wongtaisin', '黃大仙區'),
        ('yautsimmongkok', '油尖旺區')
    ) 
    
    district = models.CharField(max_length=16, choices=DISTRICT, null=True) 
    
    school_year = models.CharField(max_length=10, null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)    
    phone_no = models.CharField(max_length=50)
    fax_no = models.CharField(max_length=30)
    
    YESNO = (
        ('Y', '有'),
        ('N', '沒有')
    ) 
    
    YESNO2 = (
        ('Y', 'Yes'),
        ('N', 'No')
    )     
    
    voucher = models.CharField(max_length=1, default='N', choices=YESNO, editable=True)
    is_n_available = models.CharField(max_length=1, default='N', choices=YESNO, editable=True)
    is_hot = models.CharField(max_length=1, default='N', choices=YESNO2, editable=True)
    
    SCHOOL_CAT = (
        ('NPM', '非牟利'),
        ('PI', '私立')
    )
    
    category = models.CharField(max_length=4, choices=SCHOOL_CAT, null=True) 

    STUDENT_CAT = (
        ('COED', '男女'),
        ('SINS', '女')
    )
    
    student_category = models.CharField(max_length=4, choices=STUDENT_CAT, null=True) 

    school_url = models.CharField(max_length=300, null=True)
    highlight_url = models.CharField(max_length=200) 
    
    #tpratio_am = models.DecimalField(max_digits=3, decimal_places=1, null=True) 
    #tpratio_pm = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    
    tpratio_am = models.CharField(max_length=20, null=True) 
    tpratio_pm = models.CharField(max_length=20, null=True)
    
    vacancy_pn_list = models.TextField(null=True)    
    vacancy_n_list = models.TextField(null=True) 
    vacancy_lkg_list = models.TextField(null=True)
    vacancy_ukg_list = models.TextField(null=True)
    
    annual_fee_pn_list = models.TextField(null=True)    
    annual_fee_n_list = models.TextField(null=True) 
    annual_fee_lkg_list = models.TextField(null=True)
    annual_fee_ukg_list = models.TextField(null=True)

    CURRICULUM = (
        ('LOCAL', '本地'),
        ('NLOCAL', '非本地')
    )    
    
    curriculum = models.CharField(max_length=6, choices=CURRICULUM, null=True) 
    
    admission_dtl_url1 = models.CharField(max_length=300, null=True, blank=True)
    admission_dtl_url2 = models.CharField(max_length=300, null=True, blank=True)
    admission_url = models.CharField(max_length=300, null=True, blank=True)
    admission_url_last_hash = models.CharField(max_length=40, null=True, blank=True)
    admission_url_last_pub_date = models.DateTimeField('Date Ranked', null=True, editable=False)
    
    admission_start_date = models.DateField('Application Start date', null=True, blank=True, editable=True) 
    admission_end_date = models.DateField('Application Start date', null=True, blank=True, editable=True) 
    
    kgp_url = models.CharField(max_length=300, null=True)
    
    @property
    def is_new(self):
        
        if self.admission_url_last_pub_date:        
            time_dt = datetime.now() - self.admission_url_last_pub_date
            if time_dt.days < 5:
                return True
        return False

    def __str__(self):
        return str(self.school_no) + " - " + (self.name)
