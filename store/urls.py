from django.urls import path, include
from . import views

app_name='store'

urlpatterns = [
    path('', views.store_list, name='store_list'),
]
