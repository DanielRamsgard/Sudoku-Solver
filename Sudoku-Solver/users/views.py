from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import JsonResponse
from django.urls import reverse

# # Create your views here.
def login(request):
    return render(request, "index_login.html")