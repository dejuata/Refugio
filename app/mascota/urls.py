from django.conf.urls import url, include
from app.mascota.views import index, mascota_view, mascota_list

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new$', mascota_view, name='mascota_crear'),
    url(r'^list$', mascota_list, name='mascota_list'),
]