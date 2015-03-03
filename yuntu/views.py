from django.shortcuts import render
from .models import Index


def index(request):
    master_title = Index.objects.get(pk=1).master_title
    slave_title = Index.objects.get(pk=1).slave_title
    about_us_string = Index.objects.get(pk=1).about_us_string
    contact_us_address = Index.objects.get(pk=1).contact_us_address
    contact_us_email = Index.objects.get(pk=1).contact_us_email

    context = {
        'master_title': master_title,
        'slave_title': slave_title,
        'about_us_string': about_us_string,
        'contact_us_address': contact_us_address,
        'contact_us_email': contact_us_email
    }

    return render(request, 'yuntu/index.html', context)


def why_choose_yuntu(request):
    context = {}
    return render(request, 'yuntu/why_choose_yuntu.html', context)
