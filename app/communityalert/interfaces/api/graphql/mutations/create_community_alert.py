import graphene
from graphql_jwt.decorators import login_required
from communityalert.adapters.persistence.repositories import DjangoCommunityAlertRepository
from communityalert.domain.entities import CommunityAlert
from communityalert.adapters.graphql.types import CommunityAlertType
from user.adapters.graphql.types import UserType


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
    def mutate(self, info, content, city, state, country, media=None):
        community_alert_repo = DjangoCommunityAlertRepository()
        data = {
            'city': city,
            'country': country,
            'state': state,
            'media': media
        }

        community_alert = CommunityAlert(author_id=info.context.user.id, content=content, **data)
        new_community_alert = community_alert_repo.create(community_alert)
        return CreateCommunityAlert(community_alert=new_community_alert, author=info.context.user)