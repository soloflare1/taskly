# tasks.views.py

from django.shortcuts import render
from django.http import HttpResponse

# views
def manager_dashboard(request):
    return render(request, "dashboard/manager-dashboard.html")


def user_dashboard(request):
    return render(request, "dashboard/user-dashboard.html")

def test(request):
    return render(request, "test.html")