from django.urls import path
from . import views
app_name='Signup'
urlpatterns = [
    path('',views.SignupPage.as_view(),name='signuppage'),

]