from django.conf.urls import url, include
from app.adopcion.views import index, SolicitudList, SolicitudCreate, SolicitudUpdate, SolicitudDelete

urlpatterns = [
    url(r'^$', index),
    url(r'^solicitud/list$', SolicitudList.as_view(), name='solicitud_list'),
    url(r'^solicitud/new$', SolicitudCreate.as_view(), name='solicitud_new'),
    url(r'^solicitud/edit/(?P<pk>\d+)/$', SolicitudUpdate.as_view(), name='solicitud_edit'),
    url(r'^solicitud/delete/(?P<pk>\d+)/$', SolicitudDelete.as_view(), name='solicitud_delete'),
]