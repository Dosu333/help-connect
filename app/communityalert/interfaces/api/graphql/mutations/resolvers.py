def mutate_community_alert(info, file):
    """
    Mutates a community alert
    """
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