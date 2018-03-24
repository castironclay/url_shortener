from django.db import models
from .utils import code_generator, create_shortcode
from django.conf import settings
# Create your models here.

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 15)

# Model manager
class ClayURLManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super(ClayURLManager, self).all(*args, **kwargs)
        qs = qs.filter(active=True)
        return qs
    #creates admin command to refresh shortcodes
    def refresh_shortcodes(self, items=None):
        qs = ClayURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items, int):
            qs = qs.order_by('-id')[:items]
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            print(q.shortcode)
            q.save()
            new_codes = 1
        return "New codes made: {i}".format(i=new_codes)


class ClayURL(models.Model):
    url         = models.CharField(max_length=220, ) #Original URL
    shortcode   = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True) #Shortened URL
    updated     = models.DateTimeField(auto_now=True) #Everytime model is saved
    timestamp   = models.DateTimeField(auto_now_add=True) #When created
    active      = models.BooleanField(default=True)
    objects     = ClayURLManager()

    # If new URL saved without shortcode this code will check to see if space is blank
    # and then create a shortcode automatically
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = code_generator()
        super(ClayURL, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
