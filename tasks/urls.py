from django.urls import path
from tasks.views import manager_dashboard, user_dashboard

urlpatterns = [
    path('dashboard/manager-dashboard/', manager_dashboard),
    path('dashboard/user-dashboard/', user_dashboard),
    # path('test/', test)
]