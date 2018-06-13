# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'some_value': 'This is a value. Value it.',
    }
    return render(request, 'index.html', context)