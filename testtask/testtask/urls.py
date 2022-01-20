from django.contrib import admin
from django.urls import path
from django.urls.conf import include
import graphql
from todolist .views import *
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('todolist.urls'))
]
