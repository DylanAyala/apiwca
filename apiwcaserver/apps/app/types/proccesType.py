from graphene_django import DjangoObjectType
import graphene


class ProcessType(graphene.ObjectType):
    result = graphene.String()
