import graphene
import graphene
import graphql_jwt

class Query(graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.relay.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.relay.Verify.Field()
    refresh_token = graphql_jwt.relay.Refresh.Field()
    delete_token_cookie = graphql_jwt.relay.DeleteJSONWebTokenCookie.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)