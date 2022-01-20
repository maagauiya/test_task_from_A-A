from django.urls import path

from .views import*

urlpatterns=[
    path('',auth,name='login'),
    path('list/<str:userid>',index,name='indexname')
]