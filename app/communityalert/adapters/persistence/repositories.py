from django.contrib.auth import get_user_model
from django.db.models import Q, Case, When, F, Value, IntegerField
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

    def get_by_location(self, user_id, location):
        user = get_user_model().objects.get(id=user_id)
        upvoted_authors = user.upvoters.all().values_list('author')

        # Filter community alerts by city, state, and country
        community_alerts = CommunityAlert.objects.filter(
            (Q(state=location['state']) &
            Q(country=location['country'])) &
            ( Q(is_flagged=False) & Q(is_reported=False))
        )

        # Annotate each alert with a priority value based on different conditions
        community_alerts = community_alerts.annotate(
            priority=Case(
                # First condition: Alerts from the user's city get higher priority
                When(city=location['city'], then=Value(1)),
                # Second condition: Alerts from authors the user has upvoted before
                When(author__in=upvoted_authors, then=Value(2)),
                default=Value(3),
                output_field=IntegerField(),
            )
        )

        # Order community alerts by priority
        community_alerts = community_alerts.order_by('priority')

        # Execute the query
        result = community_alerts.all()
        return result

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
