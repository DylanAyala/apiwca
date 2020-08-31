import graphene
import graphql_jwt
from users import schema as user_schema


class Query(user_schema.Query, graphene.ObjectType):
    pass


class Mutation(user_schema.Mutation, graphene.ObjectType):
    refresh_token = graphql_jwt.Refresh.Field()
    verity_token = graphql_jwt.Verify.Field()
    revoke_token = graphql_jwt.Revoke.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)