from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
class SignupPage(View):

    def get(self,request):
        return render(request,'SignupPage.html')
    def post(self, request):
        # Get form data from POST request
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('Signup:signuppage')

        # Check if username is unique
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose a different username.")
            return redirect('Signup:signuppage')

        # Check if email is unique
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email address already in use. Please use a different email.")
            return redirect('Signup:signuppage')

        # Create the user account
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        # Optionally, you can log the user in after signup
        # from django.contrib.auth import login
        # login(request, user)

        messages.success(request, "Account created successfully. You can now log in.")
        return redirect('main:user_profile',username=username)






