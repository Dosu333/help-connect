class CommunityAlert:
    def __init__(self, author_id, content, **extra_fields):
        self.author_id = author_id
        self.content = content
        self.media = extra_fields.get('media', None)
        self.hashtags = extra_fields.get('hashtags', None)
        self.id = extra_fields.get('id', None)
        self.city = extra_fields.get('city', None)
        self.state = extra_fields.get('state', None)
        self.country = extra_fields.get('country', None)
        self.upvote_count = extra_fields.get('upvote_count', 0)
        self.downvote_count = extra_fields.get('downvote_count', 0)
        self.is_reported = extra_fields.get('is_reported', False)
        self.is_flagged = extra_fields.get('is_flagged', False)
        self.flagged_by = extra_fields.get('flagged_by', None)
        self.reported_by = extra_fields.get('reported_by', None)
        self.upvoted_by = extra_fields.get('upvoted_by', None)
        self.downvoted_by = extra_fields.get('downvoted_by', None)
        self.date_created = extra_fields.get('date_created', None)
