# Create your views here.

from django.shortcuts import render_to_response

def api(request, month=None, day=None, year=None):
    return render_to_response('api.html')

