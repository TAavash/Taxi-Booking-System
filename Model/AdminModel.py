class AdminModel:
    def __init__(self, admin_id=0, email=None, password=None):
        self._admin_id = admin_id
        self._email = email
        self._password = password

    def get_admin_id(self):
        return self._admin_id

    def set_admin_id(self, admin_id):
        self._admin_id = admin_id

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password
