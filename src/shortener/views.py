from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from analytics.models import ClickEvent

from .models import ClayURL
from .forms import SubmitUrlForm

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Submit URL",
            "form": the_form
        }
        return render(request, "shortener/home.html",context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "PiProject.com",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url")
            obj, created = ClayURL.objects.get_or_create(url=new_url)
            context = {
                "object": obj,
                "created": created,
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/already-exists.html"

        return render(request, template, context)

#class based view
class URLRedirectView(View):
    def get(self, request, shortcode=None, *args, **kwargs):
       qs = ClayURL.objects.filter(shortcode__iexact=shortcode)
       if qs.count() != 1 and not qs.exists():
           raise Http404
       obj = qs.first()
       return HttpResponseRedirect(obj.url)
