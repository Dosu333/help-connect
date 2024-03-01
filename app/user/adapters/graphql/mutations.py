import graphene
from user.adapters.persistence.implementation import DjangoUserRepository
from user.adapters.persistence.entities import User
from .types import UserType


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