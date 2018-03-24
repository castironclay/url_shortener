from django.db import models
from shortener.models import ClayURL
# Create your models here.


class ClickEventManager(models.Manager):
    def create_event(self, instance):
        if isinstance(ClayURL, instance):
            obj, created = self.get_or_create(clay_url=instance)
            obj.count += 1
            obj.save()
            return obj.count
        return None


class ClickEvent(models.Model):
    clay_url        = models.OneToOneField(ClayURL)
    count           = models.IntegerField(default=0)
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return "{i}".format(i=self.count)