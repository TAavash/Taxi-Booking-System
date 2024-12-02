class BookingModel:
    def __init__(self, booking_id=0, pickup_date=None, pickup_location=None, drop_off_location=None,
                 pickup_time=None, booking_status=None, customer_id=None, driver_id=None, admin_id=None):
        self._booking_id = booking_id
        self._pickup_date = pickup_date
        self._pickup_location = pickup_location
        self._drop_off_location = drop_off_location
        self._pickup_time = pickup_time
        self._booking_status = booking_status
        self._customer_id = customer_id
        self._driver_id = driver_id
        self._admin_id = admin_id

    def get_booking_id(self):
        return self._booking_id

    def set_booking_id(self, booking_id):
        self._booking_id = booking_id

    def get_pickup_date(self):
        return self._pickup_date

    def set_pickup_date(self, pickup_date):
        self._pickup_date = pickup_date

    def get_pickup_location(self):
        return self._pickup_location

    def set_pickup_location(self, pickup_location):
        self._pickup_location = pickup_location

    def get_drop_off_location(self):
        return self._drop_off_location

    def set_drop_off_location(self, drop_off_location):
        self._drop_off_location = drop_off_location

    def get_pickup_time(self):
        return self._pickup_time

    def set_pickup_time(self, pickup_time):
        self._pickup_time = pickup_time

    def get_booking_status(self):
        return self._booking_status

    def set_booking_status(self, booking_status):
        self._booking_status = booking_status

    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self, customer_id):
        self._customer_id = customer_id

    def get_driver_id(self):
        return self._driver_id

    def set_driver_id(self, driver_id):
        self._driver_id = driver_id

    def get_admin_id(self):
        return self._admin_id

    def set_admin_id(self, admin_id):
        self._admin_id = admin_id
