import mysql.connector


def book(booking):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taxi_booking_system"
        )

        my_cursor = dbConnect.cursor()
        command = ("INSERT INTO `booking`(`pickup_date`, `pickup_location`, `drop_off_location`, `pickup_time`, "
                   "`customer_id`) VALUES (%s,%s,%s,%s,%s)")
        values = (booking.get_pickup_date(),
                  booking.get_pickup_location(),
                  booking.get_drop_off_location(),
                  booking.get_pickup_time(),
                  booking.get_customer_id())
        my_cursor.execute(command, values)
        dbConnect.commit()
        my_cursor.close()
        dbConnect.close()
        return True

    except Exception as error:
        print(f"{error}")
        return False
