from django.urls import path
from . import views
app_name='main'
from .views import (
    UserProfileView,
)
urlpatterns = [
    
path('user/<str:username>/', views.UserProfileView.as_view(), name='user_profile'),
path('user/<str:username>/<int:fruit_id>', views.UserProfileView.as_view()),

]