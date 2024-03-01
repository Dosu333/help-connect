class CommunityAlertRepository:
    def create(self, community_alert):
        raise NotImplementedError

    def delete(self, community_alert_id):
        raise NotImplementedError

    def get_by_id(self, community_alert_id):
        raise NotImplementedError

    def find_by_user(self, user_id):
        raise NotImplementedError

    def upvote(self):
        raise NotImplementedError

    def downvote(self):
        raise NotImplementedError

    def flag(self):
        raise NotImplementedError