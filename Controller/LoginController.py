import mysql.connector


def login_customer(customer):
    result = None
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taxi_booking_system"
        )

        my_cursor = dbConnect.cursor()
        command = "SELECT * FROM customers WHERE email=%s and password=%s"
        values = (customer.get_email(), customer.get_password())
        my_cursor.execute(command, values)
        result = my_cursor.fetchone()
        return result
        my_cursor.close()
        dbConnect.close()

    except Exception as error:
        print(f"{error}")
        return result
