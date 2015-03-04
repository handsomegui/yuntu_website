from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Index, FeatureMatrix
from .forms import SubcriptionForm


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
    feature_matrix_list = FeatureMatrix.objects.all()
    context = {
        'matrix_heads': feature_matrix_list[0],
        'feature_matrix_list': feature_matrix_list[1:]
    }
    return render(request, 'yuntu/why_choose_yuntu.html', context)


@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        form = SubcriptionForm(request.POST)
        if form.is_valid():
            email_data = form.cleaned_data
            email_address = email_data['email_address']
            context = {'email_address': email_address}
            return render(request, 'yuntu/subscribtion.html', context)
