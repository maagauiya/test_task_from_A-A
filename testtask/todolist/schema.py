import graphene
from graphene_django.types import DjangoObjectType
from .models import *


class Task_type(DjangoObjectType):
    class Meta:
        model=Todolist

class Query(graphene.ObjectType):
    all_tasks=graphene.List(Task_type)

    def resolve_all_tasks(self,info,**kwargs):
        return Todolist.objects.all()