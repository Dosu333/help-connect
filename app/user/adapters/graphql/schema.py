import graphene
import graphql_jwt
from graphql import GraphQLError
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from graphql_jwt.shortcuts import create_refresh_token, get_token
from .resolvers import resolve_whoami, resolve_users
from .types import UserType
from .mutations import CreateUser
from .jwt import ObtainJSONWebToken


class Query(graphene.ObjectType):
    whoami = graphene.Field(UserType)
    users = graphene.List(UserType)
    def resolve_whoami(self, info):
        return resolve_whoami(info)
        
    @login_required
    def resolve_users(self, info):
        return resolve_users(info)

class Mutation(graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)