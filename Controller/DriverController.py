import mysql.connector


def register_driver(driver):
    try:
        dbConnect = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="taxi_booking_system"
        )

        my_cursor = dbConnect.cursor()
        command = ("INSERT INTO `drivers`(`driver_id`, `name`, `address`, `phone_number`, `email`, `password`, "
                   "`license_plate_num`) VALUES (%s,%s,%s,%s,%s,%s,%s)")
        values = (
            driver.get_driver_id(),
            driver.get_name(),
            driver.get_address(),
            driver.get_phone_number(),
            driver.get_email(),
            driver.get_password(),
            driver.get_license_plate_num()
        )

        my_cursor.execute(command, values)
        dbConnect.commit()
        my_cursor.close()
        dbConnect.close()
        return True

    except Exception as error:
        print(f"{error}")
