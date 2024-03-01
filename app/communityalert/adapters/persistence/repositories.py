from django.contrib.auth import get_user_model
from communityalert.models import CommunityAlert
from communityalert.domain.repositories import CommunityAlertRepository


class DjangoCommunityAlertRepository(CommunityAlertRepository):
    def create(self, community_alert):
        author = get_user_model().objects.get(id=community_alert.author_id)
        community_alert_data = {
            'media': community_alert.media,
            'city': community_alert.city,
            'state': community_alert.state,
            'country': community_alert.country
        }
        new_community_alert = CommunityAlert.objects.create(
            author=author,
            content=community_alert.content,
            **community_alert_data
        )
        return new_community_alert

    def delete(self, community_alert_id):
        community_alert = CommunityAlert.objects.get(id=community_alert_id)
        community_alert.delete()

    def get_by_id(self, community_alert_id):
        community_alert = CommunityAlert.objects.get(id=community_alert_id)
        return community_alert

    def find_by_user(self, user_id):
        community_alerts = CommunityAlert.objects.filter(author__id=user_id)
        return community_alerts

    def upvote(self, community_alert_id, user_id):
        user = get_user_model().objects.get(id=user_id)
        community_alert = CommunityAlert.objects.get(id=community_alert_id)

        if community_alert.downvoted_by.filter(id=user.id).exists():
            community_alert.downvote_count -= 1
            community_alert.downvoted_by.remove(user)

        community_alert.upvote_count += 1
        community_alert.upvoted_by.add(user)
        community_alert.save()

    def downvote(self, community_alert_id, user_id):
        user = get_user_model().objects.get(id=user_id)
        community_alert = CommunityAlert.objects.get(id=community_alert_id)

        if community_alert.upvoted_by.filter(id=user.id).exists():
            community_alert.upvote_count -= 1
            community_alert.upvoted_by.remove(user)

        community_alert.downvote_count += 1
        community_alert.downvoted_by.add(user)
        community_alert.save()

    def flag(self, community_alert_id, user_id):
        user = get_user_model().objects.get(id=user_id)
        community_alert = CommunityAlert.objects.get(id=community_alert_id)
        community_alert.flagged_by.add(user)
        community_alert.save()