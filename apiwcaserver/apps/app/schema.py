import graphene
from .queries.ProcessQuery import ProcessQuery
from .mutations.kill_minecraft import KillMinecraft


class Query(ProcessQuery):
    pass


class Mutation(graphene.ObjectType):
    kill_minecraft = KillMinecraft.Field()
