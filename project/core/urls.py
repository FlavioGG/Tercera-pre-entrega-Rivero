from django.urls import path

app_name = 'core'

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]