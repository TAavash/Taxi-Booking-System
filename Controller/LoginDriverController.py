import mysql.connector


def login_driver(drivers):
    result = None
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taxi_booking_system"
        )

        my_cursor = dbConnect.cursor()
        command = "SELECT * FROM drivers WHERE email=%s and password=%s"
        values = (drivers.get_email(), drivers.get_password())
        my_cursor.execute(command, values)
        result = my_cursor.fetchone()
        return result
        my_cursor.close()
        dbConnect.close()

    except Exception as error:
        print(f"{error}")
        return result
