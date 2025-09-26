from django.urls import path

from . import views


app_name = "playground"

urlpatterns = [
    path('home/', views.home_page, name="home"),
]