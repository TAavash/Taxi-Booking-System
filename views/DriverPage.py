from tkinter import *
from tkinter import messagebox, ttk

import Global
import mysql.connector
from tkcalendar import DateEntry

from PIL import Image as PILImage, ImageTk


class DriverPage:

    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title('Safe Taxi Booking (Driver)')
        self.root.resizable(False, False)
        self.root.config(bg="#FBC207")

        self.menubar = Menu(self.root)

        self.profile_menu = Menu(self.menubar, tearoff=0)
        self.profile_menu.add_command(label="Switch Account", command=self.open_login)
        self.profile_menu.add_separator()
        self.profile_menu.add_command(label="Register new Account", command=self.open_signup)
        self.profile_menu.add_separator()
        self.profile_menu.add_command(label="Logout", command=self.open_booking)
        self.profile_menu.add_separator()
        self.profile_menu.add_command(label="Close Without Question", command=exit)

        self.menubar.add_cascade(menu=self.profile_menu, label="Profile")

        self.root.config(menu=self.menubar)

        self.logo = ImageTk.PhotoImage(PILImage.open("../images/Logo.png"))
        self.root.iconphoto(True, self.logo)

        self.pnlBody = Frame(self.root, bg="black")
        self.pnlBody.place(x=0, y=0, height=100, width=1600)
        self.pnlBody2 = Frame(self.root, bg="#FBC207")
        self.pnlBody2.place(x=0, y=100, height=750, width=1600)

        self.image1 = ImageTk.PhotoImage(PILImage.open("../images/Logo.png"))

        self.image1_label = Label(image=self.image1, bg="black")
        self.image1_label.image = self.pnlBody
        self.image1_label.place(x=20, y=20)

        self.image2 = ImageTk.PhotoImage(PILImage.open("../images/traffic light.png"))

        self.image2_label = Label(image=self.image2, bg="white", bd=0)
        self.image2_label.image = self.image2
        self.image2_label.place(x=1005, y=100)

        self.image3 = ImageTk.PhotoImage(PILImage.open("../images/Taxi Intro.png"))

        self.image3_label = Label(image=self.image3, bg="black", borderwidth=0)
        self.image3_label.image = self.pnlBody2
        self.image3_label.place(x=20, y=120)

        self.image4 = ImageTk.PhotoImage(PILImage.open("../images/Taxi Facilities.png"))

        self.image4_label = Label(image=self.image4, bg="black", borderwidth=0)
        self.image4_label.image = self.pnlBody2
        self.image4_label.place(x=30, y=600)

        lbl_1 = Label(self.root, text="SAFE TRAVELLING", width=15, font=('bold', 20), bg="black", fg="yellow")
        lbl_1.place(x=90, y=30)

        self.home_button = Button(self.pnlBody, text='HOME', height=2, width=10, bg="#1f2b22", bd=0, fg='light green',
                                  command=self.home_print)
        self.home_button.place(x=500, y=40)
        self.driver_button = Button(self.pnlBody, text='DRIVER', height=2, width=10, bg="#1f2b22", bd=0,
                                    fg='light green', command=self.driver)
        self.driver_button.place(x=600, y=40)
        self.list_button = Button(self.pnlBody, text='BOOKING LIST', height=2, width=10, bg="#1f2b22", bd=0,
                                  fg='light green', command=self.list)
        self.list_button.place(x=700, y=40)
        self.about_button = Button(self.pnlBody, text='ABOUT US', height=2, width=10, bg="#1f2b22", bd=0,
                                   fg='light green', command=self.about_us)
        self.about_button.place(x=800, y=40)

        self.initial_state = {
            "result_label_text": "",
            "txt_pickup_time_text": "",
            "txt_pickup_text": "",
            "txd_drop_off_text": "",
            "txt_pickup_date_text": "",
            "txtHelp_text": "",
            "entry_fields_visible": True
        }

        self.result_label = Label(self.pnlBody2, text="", font=("bold", 12), bg="#FBC207")
        self.result_label.place(x=10, y=10, height=720, width=900)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def home_print(self):
        self.reset_label()
        self.image3 = ImageTk.PhotoImage(PILImage.open("../images/Taxi Intro.png"))

        self.image3_label = Label(image=self.image3, bg="black", borderwidth=0)
        self.image3_label.image = self.result_label
        self.image3_label.place(x=20, y=120)

        self.image4 = ImageTk.PhotoImage(PILImage.open("../images/Taxi Facilities.png"))

        self.image4_label = Label(image=self.image4, bg="black", borderwidth=0)
        self.image4_label.image = self.result_label
        self.image4_label.place(x=30, y=600)

    def driver(self):

        self.driver_panel = Label(self.result_label, text="", font=("bold", 12))
        self.driver_panel.place(x=10, y=10, height=680, width=890)

        self.update_button = Button(self.driver_panel, text="Update", command=self.update_status)
        self.update_button.place(x=50, y=450)

        self.driver_label = Label(self.driver_panel, text="Driver Details:", font=("bold", 20))
        self.driver_label.place(x=10, y=40)
        self.status_label = Label(self.driver_panel, text="Status:")
        self.status_label.place(x=10, y=500)

        self.listStatus = ['Active', 'Booked', 'Driver Busy']
        self.stats = StringVar()
        self.txt_status = OptionMenu(self.driver_panel, self.stats, *self.listStatus)
        self.txt_status.config(width=18, bg="white")
        self.stats.set('Confirm your Status')
        self.txt_status.place(x=130, y=500)

        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=30)

        self.driver_table_model = ttk.Treeview(self.driver_panel, columns=(
            "Driver ID", "Name", "Address", "Phone Number", "Email", "Password", "License Plate Number", "Status"),
                                        show="headings")
        self.driver_table_model.heading("Driver ID", text="Driver ID")
        self.driver_table_model.heading("Name", text="Name")
        self.driver_table_model.heading("Address", text="Address")
        self.driver_table_model.heading("Phone Number", text="Phone Number")
        self.driver_table_model.heading("Email", text="Email")
        self.driver_table_model.heading("Password", text="Password")
        self.driver_table_model.heading("License Plate Number", text="License Plate Number")
        self.driver_table_model.heading("Status", text="Status")

        self.driver_table_model.column("Driver ID", width=80)
        self.driver_table_model.column("Name", width=100)
        self.driver_table_model.column("Address", width=100)
        self.driver_table_model.column("Phone Number", width=100)
        self.driver_table_model.column("Email", width=120)
        self.driver_table_model.column("Password", width=80)
        self.driver_table_model.column("License Plate Number", width=120)
        self.driver_table_model.column("Status", width=80)

        self.driver_table_model.place(x=10, y=100)

        try:
            dbConnect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taxi_booking_system"
            )

            cursor = dbConnect.cursor()
            cursor.execute(f"SELECT * FROM drivers WHERE `driver_id`={Global.driver_information[0]}")
            rows = cursor.fetchall()
            for row in rows:
                self.driver_table_model.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5]
                                                                  , row[6], row[7]))

        except Exception as err:
            print(f"{err}")

        self.reset_label()

    def update_status(self):
        selected_item = self.driver_table_model.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a valid row.")
            return

        status = self.stats.get()

        self.driver_table_model.item(selected_item, values=(status,))

        try:
            dbConnect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taxi_booking_system"
            )

            cursor = dbConnect.cursor()

            query = "UPDATE `drivers` SET `status`=%s WHERE `driver_id`=%s"
            values = (status, Global.driver_information[0])

            cursor.execute(query, values)
            dbConnect.commit()

            messagebox.showinfo("Success", "Status updated successfully.")

            cursor.execute(f"SELECT * FROM drivers WHERE `driver_id`={Global.driver_information[0]}")
            updated_data = cursor.fetchone()

            self.driver_table_model.item(selected_item, values=updated_data)

        except Exception as err:
            print(f"{err}")

    def list(self):
        self.reset_label()

        self.list_panel = Label(self.result_label, text="", font=("bold", 12))
        self.list_panel.place(x=10, y=10, height=680, width=890)

        self.status_label2 = Label(self.list_panel, text="Status:")
        self.status_label2.place(x=10, y=40)

        self.list_status = ['Booked', 'Completed']
        self.stat = StringVar()
        self.txt_status2 = OptionMenu(self.list_panel, self.stat, *self.list_status)
        self.txt_status2.config(width=15, bg="white")
        self.stat.set('Booked')
        self.txt_status2.place(x=130, y=40)
        self.txt_booking = ttk.Entry(self.list_panel)
        self.txt_booking.place(x=1130, y=2120)

        self.update_btn = Button(self.list_panel, text="Update", command=self.update_booking)
        self.update_btn.place(x=10, y=240)

        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=30)

        self.table_model = ttk.Treeview(self.list_panel, columns=(
            "Booking ID", "Pickup Date", "Pickup Location", "Drop-off Location", "Pickup Time", "Cost", "Status"),
                                        show="headings")
        self.table_model.heading("Booking ID", text="Booking ID")
        self.table_model.heading("Pickup Date", text="Pickup Date")
        self.table_model.heading("Pickup Location", text="Pickup Location")
        self.table_model.heading("Drop-off Location", text="Drop-off Location")
        self.table_model.heading("Pickup Time", text="Pickup Time")
        self.table_model.heading("Cost", text="Cost")
        self.table_model.heading("Status", text="Status")

        self.table_model.column("Booking ID", width=80)
        self.table_model.column("Pickup Date", width=100)
        self.table_model.column("Pickup Location", width=120)
        self.table_model.column("Drop-off Location", width=120)
        self.table_model.column("Pickup Time", width=80)
        self.table_model.column("Cost", width=80)
        self.table_model.column("Status", width=150)

        self.table_model.place(x=10, y=280)

        try:
            dbConnect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taxi_booking_system"
            )

            cursor = dbConnect.cursor()
            cursor.execute(f"SELECT * FROM booking where `driver_id` = {Global.driver_information[0]}")
            rows = cursor.fetchall()
            for row in rows:
                self.table_model.insert("", "end",
                                        values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        except Exception as err:
            print(f"{err}")

    def update_booking(self):
        selected_items = self.table_model.selection()
        if not selected_items:
            messagebox.showerror("Error", "Please select a valid row.")
            return

        status = self.stat.get()
        booking_id = self.txt_booking.get()

        try:
            dbConnect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taxi_booking_system"
            )

            cursor = dbConnect.cursor()

            query = "UPDATE `booking` SET `status`=%s WHERE `booking_id`=%s"

            # cursor.execute(query, (status, Global.driver_information[0]))
            values = (status, booking_id)
            cursor.execute(query, values)
            dbConnect.commit()

            messagebox.showinfo("Success", "Status updated successfully.")

            cursor.execute(f"SELECT * FROM booking WHERE `driver_id`=%s")
            updated_data = cursor.fetchone()

            self.table_model.item(selected_items, values=updated_data)

        except Exception as err:
            print(f"{err}")

    def about_us(self):
        self.reset_label()

        self.about_us_panel = Label(self.result_label, text="", font=("bold", 12))
        self.about_us_panel.place(x=10, y=10, height=680, width=890)

        name = "SAFE TAXI BOOKING SYSTEM"
        email = "safetaxitrip123@gmail.com"
        contact = "+977 9xxxx xxxxx"
        country = "Nepal"
        font_size = 30

        self.about_us_panel.config(
            bg="#FBC207",
            text=f"Company Name: {name}\nEmail: {email}\nContact number: {contact}\nCountry: {country}",
            font=("Arial", font_size)
        )

        self.reset_button1()

    def reset_gui(self):

        self.result_label.config(text=self.initial_state["result_label_text"])
        self.image3_label.place_forget()
        self.image4_label.place_forget()

    def reset_label(self):
        self.reset_gui()

    def reset_button1(self):

        self.driver_panel.place_forget()

    def reset_lbl(self):
        # self.result_label.config(text=self.initial_state["result_label_text"])
        self.about_us_panel.place_forget()

    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message="Do you really want to quit?"):
            self.root.destroy()

    def open_login(self):
        from Login import Login
        self.root.destroy()

        Login_window = Tk()
        Login(Login_window)
        Login_window.mainloop()

    def open_signup(self):
        from Signup import Signup
        self.root.destroy()

        signup_window = Tk()
        Signup(signup_window)
        signup_window.mainloop()

    def open_booking(self):
        from BookingPage import BookingPage
        self.root.destroy()

        booking_window = Tk()
        BookingPage(booking_window)
        booking_window.mainloop()


if __name__ == '__main__':
    driver = Tk()
    DriverPage(driver)
    driver.mainloop()
