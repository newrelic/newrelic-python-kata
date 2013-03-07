from math import factorial

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page

from .forms import NumberForm


def factorial_h(request):
    res = ''
    if request.method == 'POST': 
        form = NumberForm(request.POST)
        if form.is_valid():
            res = factorial(form.cleaned_data['number'])
    else:
        form = NumberForm()

    return render(request, 'factorial/factorial.html', {'res': res, 'form':form})
