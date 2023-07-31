from django.urls import path
from . import views
app_name='Login'
urlpatterns = [
    path('',views.Login.as_view(),name='loginpage'),


]