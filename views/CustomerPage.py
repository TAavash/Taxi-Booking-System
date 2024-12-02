from tkinter import *
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
import Global
from PIL import Image as PILImage, ImageTk
from Model.BookingModel import BookingModel
from Controller.BookingController import book
import mysql.connector


class CustomerPage:

    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title('Safe Taxi Booking')
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

        self.image2 = ImageTk.PhotoImage(PILImage.open("../images/TRIP.png"))

        self.image2_label = Label(image=self.image2, bg="white", bd=0)
        self.image2_label.image = self.image2
        self.image2_label.place(x=925, y=100)

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
        self.ride_button = Button(self.pnlBody, text='BOOK A RIDE', height=2, width=10, bg="#1f2b22", bd=0,
                                  fg='light green', command=self.ride)
        self.ride_button.place(x=600, y=40)
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

        self.home_panel = Label(self.result_label, text="", font=("bold", 12), bg="#FBC207")
        self.home_panel.place(x=10, y=10, height=710, width=890)

        self.image3 = ImageTk.PhotoImage(PILImage.open("../images/Taxi Intro.png"))

        self.image3_label = Label(image=self.image3, bg="black", borderwidth=0)
        self.image3_label.image = self.home_panel
        self.image3_label.place(x=20, y=120)

        self.image4 = ImageTk.PhotoImage(PILImage.open("../images/Taxi Facilities.png"))

        self.image4_label = Label(image=self.image4, bg="black", borderwidth=0)
        self.image4_label.image = self.home_panel
        self.image4_label.place(x=30, y=600)

    def ride(self):

        self.ride_panel = Label(self.result_label, text="", font=("bold", 12), bg="#FBC207")
        self.ride_panel.place(x=10, y=10, height=680, width=890)

        self.pickup_date_label = Label(self.ride_panel, text="Pickup Date", width=15, font=("bold", 20), fg='red',
                                       bg="#FBC207")
        self.pickup_date_label.place(x=100, y=180)
        self.pickup_label = Label(self.ride_panel, text="Pickup Location", width=15, font=("bold", 20), fg='red',
                                  bg="#FBC207")
        self.pickup_label.place(x=100, y=240)
        self.drop_off_label = Label(self.ride_panel, text="Drop off Location", width=15, font=("bold", 20), fg='red',
                                    bg="#FBC207")
        self.drop_off_label.place(x=100, y=300)
        self.pickup_time_label = Label(self.ride_panel, text="Pickup Time", width=15, font=("bold", 20), fg='red',
                                       bg="#FBC207")
        self.pickup_time_label.place(x=100, y=360)

        self.txt_pickup_date = DateEntry(self.ride_panel, bg="white")
        self.txt_pickup_date.place(x=350, y=180, height=35, width=150)
        self.txt_pickup = Entry(self.ride_panel, bg="white")
        self.txt_pickup.place(x=350, y=240, height=35, width=150)
        self.txd_drop_off = Entry(self.ride_panel, bg="white")
        self.txd_drop_off.place(x=350, y=300, height=35, width=150)
        self.txt_pickup_time = Entry(self.ride_panel, bg="white")
        self.txt_pickup_time.place(x=350, y=360, height=35, width=150)

        self.submit_button = Button(self.ride_panel, text='Submit', height=2, width=10, bg="#1f2b22", bd=0,
                                    fg='light green', command=self.book_taxi)
        self.submit_button.place(x=600, y=270)

        self.initial_state["txt_pickup_time_text"] = ""
        self.initial_state["txt_pickup_text"] = ""
        self.initial_state["txd_drop_off_text"] = ""
        self.initial_state["txt_pickup_date_text"] = ""

        self.initial_state["entry_fields_visible"] = True

        self.reset_label()

    def list(self):
        self.reset_label()

        self.list_panel = Label(self.result_label, text="", font=("bold", 12))
        self.list_panel.place(x=10, y=10, height=680, width=890)

        self.pickup_date_label2 = Label(self.list_panel, text="Pickup Date:")
        self.pickup_date_label2.place(x=10, y=40)
        self.pickup_location_label2 = Label(self.list_panel, text="Pickup Location:")
        self.pickup_location_label2.place(x=10, y=80)
        self.drop_off_location_label2 = Label(self.list_panel, text="Drop-off Location:")
        self.drop_off_location_label2.place(x=10, y=120)
        self.pickup_time_label2 = Label(self.list_panel, text="Pickup Time:")
        self.pickup_time_label2.place(x=10, y=160)

        self.txt_pickup_date2 = DateEntry(self.list_panel)
        self.txt_pickup_date2.place(x=130, y=40)
        self.txt_pickup2 = ttk.Entry(self.list_panel)
        self.txt_pickup2.place(x=130, y=80)
        self.txd_drop_off2 = ttk.Entry(self.list_panel)
        self.txd_drop_off2.place(x=130, y=120)
        self.txt_pickup_time2 = ttk.Entry(self.list_panel)
        self.txt_pickup_time2.place(x=130, y=160)

        self.update_btn = Button(self.list_panel, text="Update", command=self.update_booking)
        self.update_btn.place(x=10, y=240)

        self.bt = Button(self.list_panel, text="Cancel", command=self.cancel_booking)
        self.bt.place(x=130, y=240)

        self.style = ttk.Style()
        self.style.configure("Treeview", rowheight=30)

        self.table_model = ttk.Treeview(self.list_panel, columns=(
            "Booking ID", "Pickup Date", "Pickup Location", "Drop-off Location", "Pickup Time", "Cost", "Status",
            "Taxi Number"), show="headings")
        self.table_model.bind("<<TreeviewSelect>>", self.selectedRow)
        self.table_model.heading("Booking ID", text="Booking ID")
        self.table_model.heading("Pickup Date", text="Pickup Date")
        self.table_model.heading("Pickup Location", text="Pickup Location")
        self.table_model.heading("Drop-off Location", text="Drop-off Location")
        self.table_model.heading("Pickup Time", text="Pickup Time")
        self.table_model.heading("Cost", text="Cost")
        self.table_model.heading("Status", text="Status")
        self.table_model.heading("Taxi Number", text="Taxi Number")

        self.table_model.column("Booking ID", width=80)
        self.table_model.column("Pickup Date", width=100)
        self.table_model.column("Pickup Location", width=120)
        self.table_model.column("Drop-off Location", width=120)
        self.table_model.column("Pickup Time", width=80)
        self.table_model.column("Cost", width=80)
        self.table_model.column("Status", width=80)
        self.table_model.column("Taxi Number", width=120)

        self.table_model.place(x=10, y=280)

        try:
            dbConnect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taxi_booking_system"
            )

            cursor = dbConnect.cursor()

            cursor.execute(f"SELECT b.`booking_id`, b.`pickup_date`, b.`pickup_location`, b.`drop_off_location`,"
                           f" b.`pickup_time`, b.`cost`, b.`status`, d.`license_plate_num`"
                           f" FROM booking b "
                           f"JOIN drivers d ON b.`driver_id` = d.`driver_id` WHERE b.`customer_id` = {Global.customer_information[0]}")

            rows = cursor.fetchall()
            for row in rows:
                self.table_model.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

        except Exception as err:
            print(f"{err}")

    def update_booking(self):
        selected_items = self.table_model.selection()
        if not selected_items:
            messagebox.showerror("Error", "Please select a valid row.")
            return

        booking_id = self.table_model.item(selected_items, "values")[0]
        pickup_date = self.txt_pickup_date2.get()
        pickup_location = self.txt_pickup2.get()
        drop_off_location = self.txd_drop_off2.get()
        pickup_time = self.txt_pickup_time2.get()

        try:
            dbConnect = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="taxi_booking_system"
            )

            cursor = dbConnect.cursor()

            query = (f"UPDATE `booking` SET `pickup_date`=%s,`pickup_location`=%s,`drop_off_location`=%s,"
                     f"`pickup_time`=%s WHERE `booking_id`=%s")
            values = (pickup_date, pickup_location, drop_off_location, pickup_time, booking_id)

            cursor.execute(query, values)
            dbConnect.commit()

            messagebox.showinfo("Success", "Booking updated successfully.")
            cursor.execute(f"SELECT b.`booking_id`, b.`pickup_date`, b.`pickup_location`, b.`drop_off_location`, "
                           f"b.`pickup_time`, b.`cost`, b.`status`, d.`license_plate_num`"
                           f" FROM booking b "
                           f"JOIN drivers d ON b.`driver_id` = d.`driver_id` WHERE b.`customer_id` = %s")
            updated_data = cursor.fetchone()

            self.table_model.item(selected_items, values=updated_data)

        except Exception as err:
            print(f"{err}")

    def cancel_booking(self):
        selected_item = self.table_model.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a valid row.")
            return

        self.table_model.delete(selected_item)

        messagebox.showinfo("Success", "Booking canceled successfully.")

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

        self.ride_panel.place_forget()

    def reset_lbl(self):

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

    def book_taxi(self):
        pickup_date = self.txt_pickup_date.get_date()
        pickup_location = self.txt_pickup.get()
        drop_off_location = self.txd_drop_off.get()
        pickup_time = self.txt_pickup_time.get()
        booking_status = "pending"
        customer_id = Global.customer_information[0]

        # Convert pickup_date to string
        formatted_pickup_date = pickup_date.strftime("%Y-%m-%d")

        booking = BookingModel(
            pickup_date=formatted_pickup_date,
            pickup_time=pickup_time,
            drop_off_location=drop_off_location,
            pickup_location=pickup_location,
            customer_id=customer_id
        )
        booked = book(booking)

        if booked:
            messagebox.showinfo("Booked", "Booked")
        else:
            messagebox.showerror("Error", "Error")

    def selectedRow(self, event):
        selected_item = self.table_model.focus()
        values = self.table_model.item(selected_item, "values")
        self.id = StringVar()
        self.booking = Entry(textvariable=self.id)
        self.booking.place_forget()

        if values:
            self.id.set(values[0])

            self.txt_pickup_date2.delete(0, "end")
            self.txt_pickup_date2.insert(0, values[1])

            self.txt_pickup2.delete(0, "end")
            self.txt_pickup2.insert(0, values[2])

            self.txd_drop_off2.delete(0, "end")
            self.txd_drop_off2.insert(0, values[3])

            self.txt_pickup_time2.delete(0, "end")
            self.txt_pickup_time2.insert(0, values[4])


if __name__ == '__main__':
    customer = Tk()
    CustomerPage(customer)
    customer.mainloop()
