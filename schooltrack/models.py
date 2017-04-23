from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class School(models.Model):
    school_no = models.CharField(max_length=8)
    location_no = models.CharField(max_length=8) 
    
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
    
    school_year = models.IntegerField(null=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)    
    phone_no = models.CharField(max_length=15)
    fax_no = models.CharField(max_length=15)
    voucher = models.CharField(max_length=1, default='N', editable=False)

    SCHOOL_CAT = (
        ('NPM', 'Non-profit-making'),
        ('PI', 'Private Independent')
    )
    
    category = models.CharField(max_length=4, choices=SCHOOL_CAT, null=True) 

    STUDENT_CAT = (
        ('COED', 'Co-educational'),
        ('SINS', 'Single Sex')
    )
    
    student_category = models.CharField(max_length=4, choices=STUDENT_CAT, null=True) 

    school_url = models.CharField(max_length=300, null=True)
    highlight_url = models.CharField(max_length=200) 
    
    tpratio_am = models.DecimalField(max_digits=3, decimal_places=1, null=True) 
    tpratio_pm = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    
    vacancy_pn_list = models.TextField(null=True)    
    vacancy_n_list = models.TextField(null=True) 
    vacancy_lkg_list = models.TextField(null=True)
    vacancy_ukg_list = models.TextField(null=True)
    
    annual_fee_pn_list = models.TextField(null=True)    
    annual_fee_n_list = models.TextField(null=True) 
    annual_fee_lkg_list = models.TextField(null=True)
    annual_fee_ukg_list = models.TextField(null=True)

    CURRICULUM = (
        ('LOCAL', 'Local'),
        ('NLOCAL', 'Non-Local')
    )    
    
    curriculum = models.CharField(max_length=6, choices=CURRICULUM, null=True) 
    
    admission_url = models.CharField(max_length=300, null=True)
    admission_url_last_hash = models.CharField(max_length=10, null=True)
    admission_url_last_pub_date = models.DateTimeField('date ranked', editable=False)
    
    def __str__(self):
        return str(self.school_no) + " - " + (self.name).encode("utf-8")
