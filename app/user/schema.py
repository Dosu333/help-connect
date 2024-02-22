import graphene
from graphql_auth.schema import UserQuery, MeQuery
from graphene_django.types import DjangoObjectType
from django.contrib.auth import get_user_model

class Query(UserQuery, MeQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)