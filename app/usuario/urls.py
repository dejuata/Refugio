from django.conf.urls import url, include

from app.usuario.views import RegistroUsuario

urlpatterns = [
    url(r'^registrar/$', RegistroUsuario.as_view(), name='registrar'),
    
]