from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    context = {}    
    return render(request, 'homepage/index.html', context)
    
