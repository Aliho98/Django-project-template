from django.shortcuts import render
from django.views import View

class LandingClass(View):
    def get(self,request):
        return render(request,'LandingPage.html')
