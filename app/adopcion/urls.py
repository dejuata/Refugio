from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required

from app.adopcion.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    url(r'^$', index),
    url(r'^solicitud/list$', login_required(SolicitudList.as_view()), name='solicitud_list'),
    url(r'^solicitud/new$', login_required(SolicitudCreate.as_view()), name='solicitud_new'),
    url(r'^solicitud/edit/(?P<pk>\d+)/$', login_required(SolicitudUpdate.as_view()), name='solicitud_edit'),
    url(r'^solicitud/delete/(?P<pk>\d+)/$', login_required(SolicitudDelete.as_view()), name='solicitud_delete'),
]