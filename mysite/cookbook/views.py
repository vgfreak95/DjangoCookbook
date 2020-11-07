from django.shortcuts import render
from django.http import HttpResponse
from .models import Cookbook
from .forms import CreateNewRecipe
from django.utils import timezone
from django.contrib.auth.models import User




# Create your views here.
def home(request):
    return render(request, 'home_view.html', {})

def about(request):
    return render(request, 'about_view.html', {})

def cookbook(request):
    
    allFood = Cookbook.objects.all()
    return render(request, 'cookbook_view.html', {"food":allFood})

def create(response):
    form = CreateNewRecipe(response.POST)
    if response.method == "POST":
        
        if form.is_valid():
            
            something = form.cleaned_data["ingredients"]
            fdnm = form.cleaned_data["name"]
            prep = form.cleaned_data["prep"]
            datetime = timezone.now()
            desc = form.cleaned_data["description"]
            userimage = form.cleaned_data["image"]
            

            query = Cookbook(foodName=fdnm, prep=prep, ingredients=something, description=desc, image=userimage)
            query.save()
            
        else:
            form = CreateNewRecipe()

    return render(response, 'createRecipe_view.html', {"form":form})





