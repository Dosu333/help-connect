import graphene
from graphql_jwt.decorators import login_required
from communityalert.adapters.persistence.repositories import DjangoCommunityAlertRepository
from communityalert.domain.entities import CommunityAlert
from communityalert.adapters.graphql.types import CommunityAlertType
from user.adapters.graphql.types import UserType
from .resolvers import mutate_community_alert


class CreateCommunityAlert(graphene.Mutation):
    author = graphene.Field(UserType)
    community_alert = graphene.Field(CommunityAlertType)

    class Arguments:
        content = graphene.String(required=True)
        media = graphene.String(required=False)
        city = graphene.String(required=True)
        state = graphene.String(required=True)
        country = graphene.String(required=True)
    
    @login_required
    def mutate(self, info,content, city, state, country, file=None):
        new_community_alert = mutate_community_alert(info, file, content, city, state, country)
        return CreateCommunityAlert(community_alert=new_community_alert, author=info.context.user)