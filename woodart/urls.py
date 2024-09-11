from django.urls import path
from woodart import views
urlpatterns = [
    path('', views.home),
]