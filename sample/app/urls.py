from django.urls import path
from .views import*
urlpatterns=[
    path('home/',Home,name='home'),
    path('',MainHome,name='mhome'),
    path('list',RegisterList,name='rlist'),
    path('edit/<int:reg_id>',RegisterUpdate.as_view(),name='ed'),
    # path('del/<int:id>',CourseDelete.as_view(),name='del')
]