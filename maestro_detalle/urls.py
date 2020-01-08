from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [url(r'^direccion$',views.DireccionList.as_view()),
              url(r'^direccion/(?P<pk>[0-9]+)$',views.DireccionDetail.as_view()),
              url(r'^persona$',views.PersonaList.as_view()),
              url(r'^persona/(?P<pk>[0-9]+)$',views.PersonaDetail.as_view()),
              ]