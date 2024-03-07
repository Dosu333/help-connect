from communityalert.adapters.persistence.repositories import DjangoCommunityAlertRepository

def resolve_retrieve_community_alert(self, info, id=None):
        community_alert_repo = DjangoCommunityAlertRepository()
        community_alert = community_alert_repo.get_by_id(id)
        return community_alert