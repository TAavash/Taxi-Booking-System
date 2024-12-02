class CustomerModel:
    def __init__(self, customer_id=0, name=None, email=None, gender=None, phone_number=None, address=None, password=None):
        self._customer_id = customer_id
        self._name = name
        self._email = email
        self._gender = gender
        self._phone_number = phone_number
        self._address = address
        self._password = password

    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_gender(self):
        return self._gender

    def set_gender(self, gender):
        self._gender = gender

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password
