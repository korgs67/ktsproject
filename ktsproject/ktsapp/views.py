from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Noutbuk
from .forms import UpdateItemForm


def show_all(request):
    noutbuks = Noutbuk.objects.all().order_by("-price")
    return render(
        request,
        'ktsapp/show_all.html',
        {'noutbuks': noutbuks}
    )


def show_all_admin(request):
    form = UpdateItemForm()
    noutbuks = Noutbuk.objects.all().order_by("-price")
    return render(
        request,
        'ktsapp/show_admin_item.html',
        {
            'form': form,
            'noutbuks': noutbuks
        }
    )

def show_item(request, item_id):
    item = Noutbuk.objects.get(pk=item_id)
    return render(
        request,
        'ktsapp/show_item.html',
        {'item': item}
    )


def update_item(request, item_id):
    if request.method == 'POST':
        print()
        new_description = dict(request.POST).get('description', '')
        new_price = dict(request.POST).get('price', '')
        Noutbuk.objects.filter(pk=item_id).update(
            price=new_price[0],
            description=new_description[0]
        )

    return redirect('admin')


def delete_item(request, item_id):
    Noutbuk.objects.filter(pk=item_id).delete()
    return redirect('admin')

def main(request):
    return redirect('main')

def page_not_found(request, *args, **argv):
    return redirect('main')
