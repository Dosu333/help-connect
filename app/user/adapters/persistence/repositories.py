from django.contrib.auth import get_user_model
from user.models import User
# from .entities import User
from user.domain.repositories import UserRepository

class DjangoUserRepository(UserRepository):
    def create(self, user):
        new_user = User.objects.create_user(
            email=user.email, 
            password=user.password, 
            first_name=user.first_name,
            last_name=user.last_name,
            phone=user.phone
        )
        return new_user

    def update(self, user):
        user_model = get_user_model().objects.get(id=user.id)
        user_model.first_name = user.first_name
        user_model.last_name = user.last_name
        user_model.phone = user.phone
        user_model.save()

    def delete(self, user_id):
        get_user_model().objects.get(id=user_id).delete()

    def find_by_email(self, email):
        return get_user_model().objects.get(email=email)

    # def get_by_id(self, user_id):
    #     user = get_user_model().objects.get(id=user_id)
    #     return User(
    #         email=user.email,
    #         first_name=user.first_name,
    #         last_name=user.last_name,
    #         phone=user.phone,
    #         is_active=user.is_active,
    #         is_staff=user.is_staff,
    #         is_superuser=user.is_superuser,
    #         verified=user.verified
    #     )