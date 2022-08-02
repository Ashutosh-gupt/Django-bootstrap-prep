from unicodedata import name
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.


def index(request):
    context = {
        'variable': 'This is a python context variable in object'
    }
    return render(request, 'index.html', context)


def about(request):
    # return HttpResponse('this is About page')
    return render(request, 'about.html')


def contact(request):
    # return HttpResponse('this is Contact page')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone,
                          desc=desc, date=datetime.today())
        contact.save()

    return render(request, 'contacts.html')


def services(request):
    # return HttpResponse('this is services page')
    return render(request, 'services.html')
