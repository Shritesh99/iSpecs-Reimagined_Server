from django.urls import path
from .views import *

urlpatterns = [
    path('', Detect.as_view()),
]