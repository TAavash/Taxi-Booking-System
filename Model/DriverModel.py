class DriverModel:
    def __init__(self, driver_id=0, name=None, address=None, phone_number=None, email=None, password=None, license_plate_num=None):
        self._driver_id = driver_id
        self._name = name
        self._address = address
        self._phone_number = phone_number
        self._email = email
        self._password = password
        self._license_plate_num = license_plate_num

    def get_driver_id(self):
        return self._driver_id

    def set_driver_id(self, driver_id):
        self._driver_id = driver_id

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_address(self):
        return self._address

    def set_address(self, address):
        self._address = address

    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    def get_email(self):
        return self._email

    def set_email(self, email):
        self._email = email

    def get_password(self):
        return self._password

    def set_password(self, password):
        self._password = password

    def get_license_plate_num(self):
        return self._license_plate_num

    def set_license_plate_num(self, license_plate_num):
        self._license_plate_num = license_plate_num
