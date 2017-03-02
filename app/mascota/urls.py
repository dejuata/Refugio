from django.conf.urls import url, include
from app.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new$', mascota_view, name='mascota_crear'),
    url(r'^list$', mascota_list, name='mascota_list'),
    url(r'^edit/(?P<id_mascota>\d+)/$', mascota_edit, name='mascota_edit'),
    url(r'^delete/(?P<id_mascota>\d+)/$', mascota_delete, name='mascota_delete'),
]