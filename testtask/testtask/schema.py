import graphene
from todolist.schema import Query as q


class Query(q):
    pass

schema=graphene.Schema(query=Query)