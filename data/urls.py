from django.urls import path 
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("new-expense/", views.new_expense, name="new-expense"),
]
