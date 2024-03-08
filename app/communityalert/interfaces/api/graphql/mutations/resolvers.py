from core.file_upload.upload import file_upload
from communityalert.adapters.persistence.repositories import DjangoCommunityAlertRepository
from communityalert.domain.entities import CommunityAlert

def mutate_community_alert(info, file, content, city, state, country):
    """
    Mutates a community alert
    """
    community_alert_repo = DjangoCommunityAlertRepository()
    media = None

    if file:
        media = file_upload(file)

    data = {
        'city': city,
        'country': country,
        'state': state,
        'media': media
    }

    community_alert = CommunityAlert(author_id=info.context.user.id, content=content, **data)
    new_community_alert = community_alert_repo.create(community_alert)
    return new_community_alert