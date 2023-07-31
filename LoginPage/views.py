from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login

class Login(View):
    def get(self,request):
        return render(request,'LoginPage.html')
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:user_profile', username=username)
        else:
            # Authentication failed, show an error message
            context = {'error_message': 'Invalid username or password'}
            return render(request, 'Login:loginpage', context)