from communityalert.adapters.persistence.repositories import DjangoCommunityAlertRepository

def resolve_all_community_alerts(info, location):
        community_alert_repo = DjangoCommunityAlertRepository()
        community_alerts = community_alert_repo.get_by_location(info.context.user.id, location)
        return community_alerts