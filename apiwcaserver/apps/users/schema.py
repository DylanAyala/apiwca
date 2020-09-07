import graphene
from .queries.me import MeQuery
from .mutations.json_web_token import ObtainJSONWebToken


class Query(MeQuery):
    pass


class Mutation(graphene.ObjectType):
    auth = ObtainJSONWebToken.Field()
