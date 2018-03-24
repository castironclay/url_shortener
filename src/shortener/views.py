from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import ClayURL

# Create your views here.
def clay_redirect_view(request, shortcode=None, *args, **kwargs):   #function based view
    obj = get_object_or_404(ClayURL, shortcode=shortcode)
    # do something
    return HttpResponseRedirect(obj.url)


class ClayCBView(View):                             #class based view
    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(ClayURL, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)

    def post(self, request, *args, **kwargs):
        return(HttpResponse)


'''    
#obj = ClayURL.objects.get(shortcode=shortcode)
    #try:
    #    obj = ClayURL.objects.get(shortcode=shortcode)
    #except:
    #    obj = ClayURL.objects.all().first()


    #obj_url = obj.url

    #obj_url = None
    #qs = ClayURL.objects.filter(shortcode__iexact=shortcode.upper())
    #if qs.exists() and qs.count() == 1:
    #    obj = qs.first()
    #    obj_url = obj.url
    '''