import graphene
import graphql_jwt
from graphql import GraphQLError
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required
from graphql_jwt.shortcuts import create_refresh_token, get_token
from .resolvers import resolve_whoami, resolve_users
from .jwt import ObtainJSONWebToken
from user.adapters.persistence.implementation import DjangoUserRepository
from user.adapters.persistence.entities import User


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)
    token = graphene.String()
    refresh_token = graphene.String()

    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        phone = graphene.String(required=False)

    def mutate(self, info, email, password, first_name, last_name, phone=None):
        user_repo = DjangoUserRepository()
        user = User(email=email, password=password,
                    first_name=first_name, last_name=last_name, phone=phone)
        new_user = user_repo.create(user)
        return CreateUser(user=new_user)


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