class UserRepository:
    def create(self, user):
        raise NotImplementedError

    def update(self, user):
        raise NotImplementedError

    def delete(self, user_id):
        raise NotImplementedError

    def get_by_id(self, user_id):
        raise NotImplementedError

    def find_by_email(self, email):
        raise NotImplementedError