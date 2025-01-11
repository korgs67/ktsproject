from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from . models import Noutbuk


def show_all(request):
    noutbuks = Noutbuk.objects.all().order_by("-price")
    return render(
        request,
        'ktsapp/show_all.html',
        {'noutbuks': noutbuks}
    )
