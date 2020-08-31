import graphene
from .queries.me import MeQuery


class Query(MeQuery):
    pass


class Mutation(graphene.ObjectType):
    pass
