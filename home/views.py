from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable": "This is sent"
    }
    return render(request, 'index.html',context)
    #return HttpResponse("This is the HOMEPAGE")


def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is the ABOUT-PAGE")


def services(request):
    return render(request, 'servives.html')
    #return HttpResponse("This is the SERVICES-PAGE")


def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("This is the CONTACT-PAGE")
