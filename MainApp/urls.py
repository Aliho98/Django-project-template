from django.urls import path
from . import views
app_name='main'
urlpatterns = [
    
path('user/<str:username>/', views.UserProfileView.as_view(), name='user_profile'),

]