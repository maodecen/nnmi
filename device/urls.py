from django.conf.urls import url
from device import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^device/', views.nodeAction, name ='nodeAction')
]