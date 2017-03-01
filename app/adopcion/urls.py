from django.conf.urls import url, include
from app.adopcion.views import index

urlpatterns = [
    url(r'^$', index),
]