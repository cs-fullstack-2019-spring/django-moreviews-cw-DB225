from django.shortcuts import render
from django.http import HttpResponse
from .models import Cup

# Create your views here.
def index(request):
    return HttpResponse("Test URL")

# Function to print hello + the name
def yourName(request, name):
    return HttpResponse("Hello "+str(name))

# Function to print the product times
def theNumb(request,number):
    return HttpResponse("The product times2 is: "+str(number))

# Function to print the sum of all numbers from 0 to the integer
def theNumb2(request,number):
    return HttpResponse("The sum of all numbers from 0 to the integer is: "+str(number))

# Function to print all entry purchaseTimes
def all(request):
    allPurchaseTimes = Cup.objects.all()
    after2012 = Cup.objects.filter(manufactuerDate__gt="2012-01-01")

    context = {
        'allPurchaseTimes': allPurchaseTimes,
        'after2012': after2012,
    }

    return render(request, 'cupApp/index.html', context)

