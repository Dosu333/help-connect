import graphene
from .types import CommunityAlertType
from .resolvers import resolve_retrieve_community_alert
from communityalert.interfaces.api.graphql.mutations.create_community_alert import CreateCommunityAlert
from communityalert.models import CommunityAlert

class Query(graphene.ObjectType):
    community_alert = graphene.List(CommunityAlertType)

    def resolve_community_alert(self, info):
        return CommunityAlert.objects.all()

class Mutation(graphene.ObjectType):
    create_community_alert = CreateCommunityAlert.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)