from django.urls import path
from .import views

urlpatterns = [
    path("", views.clientHome, name="client-home"),
    path("login", views.login, name="client-login"),
    path("register", views.register, name="client-register"),
    path("dashboard/", views.companyDashboard, name="client-dasboard"),
]