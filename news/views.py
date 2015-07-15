from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Location, User, Article

def index(request):
    template = loader.get_template('news/index.html')
    context = RequestContext(request, {
        
    })

    return HttpResponse(template.render(context))