class CommunityAlertRepository:
    def create(self, community_alert):
        raise NotImplementedError

    def delete(self, community_alert_id):
        raise NotImplementedError

    def get_by_id(self, community_alert_id):
        raise NotImplementedError

    def get_by_location(self, location):
        raise NotImplementedError

    def find_by_user(self, user_id):
        raise NotImplementedError

    def upvote(self, community_alert_id, user_id):
        raise NotImplementedError

    def downvote(self, community_alert_id, user_id):
        raise NotImplementedError

    def flag(self, community_alert_id, user_id):
        raise NotImplementedError