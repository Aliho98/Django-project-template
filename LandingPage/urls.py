from django.urls import path
from . import views
app_name='Landing'
urlpatterns = [
    path('',views.LandingClass.as_view(),name='RenderLanding')


]