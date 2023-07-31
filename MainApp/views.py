from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User


class UserProfileView(View):
    def get(self, request, username):
        # Retrieve the user object based on the username
        user = User.objects.get(username=username)

        return render(request, 'Mainapp.html', {'user': user})
