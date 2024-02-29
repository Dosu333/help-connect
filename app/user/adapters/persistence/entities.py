class User:
    def __init__(self, email, first_name, last_name, password=None, **kwargs):
        id = kwargs.get('id', None)
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone = kwargs.get('phone', None)
        self.is_active = kwargs.get('is_active', True)
        self.is_staff = kwargs.get('is_staff', False)
        self.is_superuser = kwargs.get('is_superuser', False)
        self.verified = kwargs.get('verified', False)

    def verify_user():
        self.verified = True
        return True
