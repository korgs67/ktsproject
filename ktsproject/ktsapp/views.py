from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Noutbuk


def show_all(request):
    noutbuks = Noutbuk.objects.all().order_by("-price")
    return render(
        request,
        'ktsapp/show_all.html',
        {'noutbuks': noutbuks}
    )

def main(request):
    return redirect('main')

def page_not_found(request, *args, **argv):
    return redirect('main')
