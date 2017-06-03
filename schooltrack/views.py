import urllib.request, json
from django.shortcuts import get_object_or_404, render

from .models import School
from .forms import SchoolForm

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
    
def search_school(request):

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SchoolForm(request.POST)
        # check whether it's valid:
        
        #table.objects.filter(string__icontains='pattern')
        if form.is_valid():
            # process the data in form.cleaned_data as required
             
            search_school = form.cleaned_data['search_school']
            #print("search string=" + str(search_movie))
            school_list = School.objects.filter(name__icontains=search_school)
            school_list = school_list.order_by('id')
            context = {'school_list': school_list}
            context = {**context, **label_list}

            # redirect to a new URL:
            return render(request, 'schooltrack/index.html', context)
        return HttpResponseRedirect('schooltrack/')
