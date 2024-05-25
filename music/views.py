from django.shortcuts import render, redirect







# Create your views here.

#Renders the home page
def home(request):
    return render(request, 'music/index.html')




