from django.urls import path
from .views import home

app_name = 'university'
urlpatterns = [
    path('', home, name='home'),
]