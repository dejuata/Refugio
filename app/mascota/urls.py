from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from app.mascota.views import index, listado, mascota_view, mascota_list, mascota_edit, mascota_delete, \
    MascotaList, MascotaCreate, MascotaUpdate, MascotaDelete

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^new$', login_required(MascotaCreate.as_view()), name='mascota_crear'),
    url(r'^list$', login_required(MascotaList.as_view()), name='mascota_list'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(MascotaUpdate.as_view()), name='mascota_edit'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(MascotaDelete.as_view()), name='mascota_delete'),
    url(r'^listado', listado, name='listado'),
]