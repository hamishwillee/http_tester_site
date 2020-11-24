from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.cookie_samesite_none_not_secure, name='cookie_samesite_none_not_secure'),
]
