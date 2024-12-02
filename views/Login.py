from tkinter import *
from tkinter import messagebox
import Global
from PIL import Image as PILImage, ImageTk

from Controller.LoginDriverController import login_driver
from Model.DriverModel import DriverModel
from Controller.AdminController import login_admin
from Model.AdminModel import AdminModel
from Controller.LoginController import login_customer
from Model.CustomerModel import CustomerModel
from Registration import Registration
from Signup import Signup


class Login:

    def __init__(self, root):

        self.root = root
        self.root.geometry("736x604+600+50")
        self.root.title('Login Page')
        self.root.resizable(False, False)
        self.root.config(bg="black")

        self.logo = ImageTk.PhotoImage(PILImage.open("../images/Logo.png"))
        self.root.iconphoto(True, self.logo)

        self.image = ImageTk.PhotoImage(PILImage.open("../images/11.png"))

        self.image_label = Label(image=self.image, bg="#404040")
        self.image_label.image = self.image
        self.image_label.place(x=0, y=0)

        self.lbl_title = Label(self.root, text="Taxi Booking System", width=18, font=("bold", 25), fg='white', bg="black")
        self.lbl_title.place(x=20, y=50)
        
        self.lbl_1 = Label(self.root, text="Email", width=10, font=("bold", 15), fg='white', bg="black")
        self.lbl_1.place(x=30, y=200)

        self.txtEmail = Entry(self.root, bg="light gray")
        self.txtEmail.place(x=200, y=200, height=35, width=150)

        self.lbl_2 = Label(self.root, text="Password", width=10, font=("bold", 15), fg='white', bg="black")
        self.lbl_2.place(x=50, y=260)

        self.txtPassword = Entry(self.root, show="*", bg="light gray")
        self.txtPassword.place(x=200, y=260, height=35, width=150)

        self.lbl_3 = Label(self.root, text="Dont have an account : ", width=20, font=("bold", 10), fg='white', bg="black")
        self.lbl_3.place(x=70, y=310)

        self.signup_button = Button(self.root, text='Signup', width=10, fg='#2A67F5', command=self.open_signup, bg="black", bd=0)
        self.signup_button.place(x=220, y=310)

        self.submit_button = Button(self.root, text='Submit', width=15, bg="black", fg='white', command=self.submit)
        self.submit_button.place(x=80, y=400)

        self.back_button = Button(self.root, text='Back', width=15, bg="gray", fg='black', command=self.back)
        self.back_button.place(x=220, y=400)

    def back(self):
        if messagebox.askyesno(title="Back To Booking Page", message="Are you sure you want to go back ?"):
            self.open_booking()

    def submit(self):
        email = self.txtEmail.get()
        password = self.txtPassword.get()

        customer = CustomerModel(email=email, password=password)
        registered_customer = login_customer(customer)
        admin = AdminModel(email=email, password=password)
        registered_admin = login_admin(admin)
        driver = DriverModel(email=email, password=password)
        registered_driver = login_driver(driver)

        if registered_customer is not None:
            Global.customer_information = registered_customer
            messagebox.showinfo("Welcome", f"Welcome {Global.customer_information[1]}")
            self.root.destroy()

            from CustomerPage import CustomerPage
            new_root = Tk()
            CustomerPage(new_root)
            new_root.mainloop()

        elif registered_admin is not None:
            Global.admin_information = registered_admin
            messagebox.showinfo("Welcome", f"Welcome Admin")
            self.root.destroy()

            from AdminPage import AdminPage
            new_root = Tk()
            AdminPage(new_root)
            new_root.mainloop()

        elif registered_driver is not None:
            Global.driver_information = registered_driver
            messagebox.showinfo("Welcome", f"Welcome {Global.driver_information[1]}")
            self.root.destroy()

            from DriverPage import DriverPage
            new_root = Tk()
            DriverPage(new_root)
            new_root.mainloop()

        else:
            messagebox.showinfo("Error", f"Wrong Email or Password")

    def open_registration(self):
        self.root.destroy()

        registration_window = Tk()
        Registration(registration_window)
        registration_window.mainloop()

    def open_signup(self):
        self.root.destroy()
        signup_window = Tk()
        Signup(signup_window)
        signup_window.mainloop()

    def open_booking(self):
        from BookingPage import BookingPage
        self.root.destroy()

        booking_window = Tk()
        bookingPage = BookingPage(booking_window)
        booking_window.mainloop()


if __name__ == '__main__':
    root = Tk()
    Login(root)
    root.mainloop()
