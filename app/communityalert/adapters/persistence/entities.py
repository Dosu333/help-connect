class CommunityAlert:
    def __init__(self, author, content, **kwargs):
        self.author = author,
        self.content = content,
        self.media = kwargs.get('media', None),
        self.hashtags = kwargs.get('hashtags', None),
        self.id = kwargs.get('id', None),
        self.city = kwargs.get('city', None),
        self.state = kwargs.get('state', None),
        self.country = kwargs.get('country', None),
        self.upvote_count = kwargs.get('upvote_count', 0)
        self.downvote_count = kwargs.get('downvote_count', 0)
        self.is_reported = kwargs.get('is_reported', False)
        self.is_flagged = kwargs.get('is_flagged', False)
        self.flagged_by = kwargs.get('flagged_by', None)
        self.reported_by = kwargs.get('reported_by', None)
        self.upvoted_by = kwargs.get('upvoted_by', None)
        self.downvoted_by = kwargs.get('downvoted_by', None)
        self.date_created = kwargs.get('date_created', None)
