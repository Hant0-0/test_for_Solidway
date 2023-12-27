from django.shortcuts import render

from test_list.models import Dogs


def home(request):
    dogs = Dogs.objects.all()
    return render(request, 'home.html', {'dogs': dogs})

