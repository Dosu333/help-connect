from graphene_django import DjangoObjectType
from communityalert.models import CommunityAlert

class CommunityAlertType(DjangoObjectType):
    class Meta:
        model = CommunityAlert