import graphene
from .types import CommunityAlertType
from .resolvers import resolve_retrieve_community_alert

class Query(graphene.ObjectType):
    cre