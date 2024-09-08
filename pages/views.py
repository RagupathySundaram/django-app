from django.shortcuts import render

# Create your views here.


# pages/views.py
from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("Hello, World!")

def about_page_view(request):  # new
    # return render(request, "pages/about.html")
    context = {
        "name": "Alice",
        "age": 33,  # new
    }
    return render(request, "pages/about.html", context)  # new