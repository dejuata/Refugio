from django.conf.urls import url, include
from app.mascota.views import index, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new$', MascotaCreate.as_view(), name='mascota_crear'),
    url(r'^list$', MascotaList.as_view(), name='mascota_list'),
    url(r'^edit/(?P<pk>\d+)/$', MascotaUpdate.as_view(), name='mascota_edit'),
    url(r'^delete/(?P<pk>\d+)/$', MascotaDelete.as_view(), name='mascota_delete'),
]