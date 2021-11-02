from django.urls import path
from . import views

# URLConfig
urlpatterns = [
  path('playground/hello', views.say_hello)
]