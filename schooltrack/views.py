import urllib.request, json
from django.shortcuts import get_object_or_404, render

from .models import School

def index(request):
    school_list = School.objects.filter(district="central")
    school_list = School.objects.order_by('id')
    context = {'school_list': school_list}    
    return render(request, 'schooltrack/index.html', context)
	
def filter(request, district_filter=None):
    if district_filter == "None":
        district_filter = None
    school_list = School.objects.filter(district=district_filter)
    school_list = school_list.order_by('id')
    context = {'school_list': school_list}    
    return render(request, 'schooltrack/index.html', context)
