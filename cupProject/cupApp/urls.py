from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    # "hello" route that takes a name in the URL and returns a response with "hello [NAME]".
    path('hello/<str:name>/', views.yourName, name="yourName"),

    # "times2" route that takes an argument in the URL and returns a response with "The product times 2 is: [ANSWER]"
    path('times2/<int:number>/', views.theNumb, name="theNumb"),

    # "total" route that takes an integer in the URL and returns a response with "The sum of all numbers from 0 to the integer is: [SUM]"
    path('total/<int:number>/', views.theNumb2, name="theNumb2"),

    # 'all/' endpoint that prints out all entry purchaseTimes
    path('all/', views.all, name="all"),
]