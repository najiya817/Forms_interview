from django.urls import path
from .views import*
urlpatterns=[
    path('',NewPage,name='new'),
]