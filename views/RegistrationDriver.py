from tkinter import *
from Model.DriverModel import DriverModel
from Controller.DriverController import register_driver
from tkinter import messagebox

from PIL import Image as PILImage, ImageTk


class RegistrationDriverForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry("700x600")
        self.root.config(bg="white")
        self.root.title('Registration form')
        self.root.resizable(False, False)
        self.logo = ImageTk.PhotoImage(PILImage.open("../images/Logo.png"))
        self.root.iconphoto(True, self.logo)

        self.image = ImageTk.PhotoImage(PILImage.open("../images/33.png"))

        self.image_label = Label(image=self.image, bg="white")
        self.image_label.image = self.image
        self.image_label.place(x=0, y=0)

        self.create_widgets()

    def create_widgets(self):
        lbl_0 = Label(self.root, text="Driver Registration Form", width=22, font=("Times New Roman", 20), bg="white")
        lbl_0.place(x=30, y=60)

        lbl_1 = Label(self.root, text="FullName", width=15, font=("bold", 10), bg="white")
        lbl_1.place(x=40, y=130)
        self.enter_1 = Entry(self.root, bg="light gray")
        self.enter_1.place(x=220, y=130)

        lbl_2 = Label(self.root, text="Address", width=15, font=("bold", 10), bg="white")
        lbl_2.place(x=28, y=180)
        self.enter_2 = Entry(self.root, bg="light gray")
        self.enter_2.place(x=220, y=180)

        lbl_3 = Label(self.root, text="Phone Number", width=15, font=('bold', 10), bg="white")
        lbl_3.place(x=40, y=230)
        self.enter_3 = Entry(self.root, bg="light gray")
        self.enter_3.place(x=220, y=230)

        lbl_4 = Label(self.root, text="Email", width=10, font=('bold', 10), bg="white")
        lbl_4.place(x=40, y=280)
        self.enter_4 = Entry(self.root, bg="light gray")
        self.enter_4.place(x=220, y=280)

        lbl_5 = Label(self.root, text="Password", width=12, font=('bold', 10), bg="white")
        lbl_5.place(x=40, y=330)
        self.enter_5 = Entry(self.root, bg="light gray")
        self.enter_5.place(x=220, y=330)
        self.enter_5.config(show="*")

        lbl_6 = Label(self.root, text="License Plate No.", width=15, font=('bold', 10), bg="white")
        lbl_6.place(x=40, y=380)
        self.enter_6 = Entry(self.root, bg="light gray")
        self.enter_6.place(x=220, y=380)

        lbl_7 = Label(self.root, text="License Image", width=15, font=('bold', 10), bg="white")
        lbl_7.place(x=40, y=430)
        self.image = ImageTk.PhotoImage(PILImage.open("../images/upload.png"))

        self.image_label = Label(image=self.image, bg="black")
        self.image_label.image = self.image
        self.image_label.place(x=220, y=430)

        submit_button = Button(self.root, text='Submit', width=15, bg="#3366FF", fg='white', command=self.submit)
        submit_button.place(x=100, y=500)
        back_button = Button(self.root, text='Back', width=15, bg="light gray", command=self.back)
        back_button.place(x=250, y=500)

    def open_login(self):
        from Login import Login
        self.root.destroy()

        Login_window = Tk()
        login = Login(Login_window)
        Login_window.mainloop()

    def submit(self):
        full_name = self.enter_1.get()
        address = self.enter_2.get()
        phone = self.enter_3.get()
        email = self.enter_4.get()
        password = self.enter_5.get()
        license = self.enter_6.get()

        driver = DriverModel(name=full_name,address=address,phone_number=phone,email=email,password=password,
                             license_plate_num=license)
        registered = register_driver(driver)
        if registered:
            messagebox.showinfo("Registered","Registered Successfully")

    def back(self):
        if messagebox.askyesno(title="Back To Login Page", message="Are you sure you want to go back ?"):
            self.open_login()


if __name__ == "__main__":
    root = Tk()
    RegistrationDriverForm(root)
    root.mainloop()
