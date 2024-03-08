import graphene
from .types import CommunityAlertType
from .resolvers import resolve_all_community_alerts
from communityalert.interfaces.api.graphql.mutations.create_community_alert import CreateCommunityAlert
from communityalert.models import CommunityAlert


class Query(graphene.ObjectType):
    all_community_alerts = graphene.List(
                                CommunityAlertType, 
                                city=graphene.String(), 
                                state=graphene.String(), 
                                country=graphene.String()
                            )

    def resolve_all_community_alerts(self, info, city, state, country):
        location = {'city': city, 'state': state, 'country': country}
        return resolve_all_community_alerts(info, location)


class Mutation(graphene.ObjectType):
    create_community_alert = CreateCommunityAlert.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
