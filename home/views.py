from django.shortcuts import render, HttpResponse

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
    return render(request, 'contacts.html')


def services(request):
    # return HttpResponse('this is services page')
    return render(request, 'services.html')
