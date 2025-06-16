from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.views_login, name='login'),
    path('signup/', views.views_signup, name='signup'),
    path('logout/', views.views_logout, name='logout'),
]

