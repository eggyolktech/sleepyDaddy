import urllib.request, json
from django.shortcuts import get_object_or_404, render

from .models import School

YESNO = (
    ('Y', '有'),
    ('N', '沒有')
) 

label_list = {
    'yes_no_list': YESNO,
    'district_list': School.DISTRICT,
    'school_cat_list': School.SCHOOL_CAT,
    'student_cat_list': School.STUDENT_CAT,
    'curriculum_list': School.CURRICULUM
}

def index(request):
    school_list = School.objects.filter(district="central")
    school_list = School.objects.order_by('id')
    context = {'school_list': school_list}
    context = {**context, **label_list}
    return render(request, 'schooltrack/index.html', context)
	
def district(request, district_filter=None):
    if district_filter == "None":
        district_filter = None
    school_list = School.objects.filter(district=district_filter)
    school_list = school_list.order_by('id')
    context = {'school_list': school_list}
    context = {**context, **label_list}
    return render(request, 'schooltrack/index.html', context)

def hot(request):
    school_list = School.objects.filter(is_hot="Y")
    school_list = school_list.order_by('id')
    context = {'school_list': school_list}
    context = {**context, **label_list}
    return render(request, 'schooltrack/index.html', context)
