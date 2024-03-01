from communityalert.models import CommunityAlert
from .repositories import CommunityAlertRepository

class DjangoCommunityRepository(CommunityAlertRepository):
    def create(self, user):
        new_user = CommunityAlert.objects.create_user(
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