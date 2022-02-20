from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='home'),
        path('layout', views.about, name='about'),
        path('nom', views.prod, name='prod'),
        path('comms', views.comm, name='comm')
]
