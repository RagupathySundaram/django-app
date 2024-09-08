from django.shortcuts import render

# Create your views here.


# pages/views.py
from django.http import HttpResponse


from django.views.generic import TemplateView  # new


def home_page_view(request):
    # return HttpResponse("Hello, World!")

    context = {  # new
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "THAnk you FOR visitING.",
    }
    return render(request, "home.html", context)

def about_page_view(request):  # new
    return render(request, "pages/about.html")

    context = {
        "name": "Alice",
        "age": 33,  # new
    }
    return render(request, "pages/about.html", context)  # new

class AboutPageView(TemplateView):  # new
 template_name = "about.html"
 def get_context_data(self, **kwargs):  # new
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main Street"
        context["phone_number"] = "555-555-5555"
        return context