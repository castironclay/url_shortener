from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import ClayURL

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "shortener/home.html", {})

'''
def clay_redirect_view(request, shortcode=None, *args, **kwargs):   #function based view
    obj = get_object_or_404(ClayURL, shortcode=shortcode)
    return HttpResponseRedirect(obj.url)
'''

class ClayCBView(View):                             #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ClayURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)
    def post(self, request, *args, **kwargs):
        return(HttpResponse)


