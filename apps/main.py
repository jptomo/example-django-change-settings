from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse


def index(request):
    return HttpResponse(getattr(settings, 'MESSAGE', '!!! EMPTY !!!'))


urlpatterns = url(r'^$', index),
