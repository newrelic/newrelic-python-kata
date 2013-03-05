from .models import Poll
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

def index(request):
    poll_list = Poll.objects.all()
    #poll_list = Poll.objects.all().prefetch_related('choice_set')
    return render(request, 'query/index.html', {'poll_list': poll_list})

def name_filter(request):
    poll_list = Poll.objects.all()
    #poll_list = Poll.objects.filter(question__contains='x').prefetch_related('choice_set')
    return render(request, 'query/name_filter.html', {'poll_list':poll_list})

