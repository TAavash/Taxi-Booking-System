import mysql.connector


def register(customer):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taxi_booking_system"
        )

        my_cursor = dbConnect.cursor()
        command = ("INSERT INTO `customers`(`customer_id`, `name`, `email`, `gender`, `phone_number`, `address`, "
                   "`password`) VALUES (%s,%s,%s,%s,%s,%s,%s)")
        values = (customer.get_customer_id(),
                  customer.get_name(),
                  customer.get_email(),
                  customer.get_gender(),
                  customer.get_phone_number(),
                  customer.get_address(),
                  customer.get_password())
        my_cursor.execute(command, values)
        dbConnect.commit()
        my_cursor.close()
        dbConnect.close()
        return True

    except Exception as error:
        print(f"{error}")
