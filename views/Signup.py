from tkinter import *
from tkinter import PhotoImage
from PIL import Image as PILImage, ImageTk


class Signup:

    def __init__(self, root):
        self.root = root
        self.root.geometry("400x200+500+300")
        self.root.title('Sign up')
        self.root.resizable(False, False)
        self.root.config(bg="black")

        # self.logo = ImageTk.PhotoImage(PILImage.open("../images/Logo.png"))
        # self.root.iconphoto(True, self.logo)

        self.logo_file = "../images/Logo.png"
        self.logo = PhotoImage(file=self.logo_file)
        self.root.iconphoto(True, self.logo)

        self.lbl_1 = Label(self.root, text="Register as :", width=18, font=("bold", 20), bg="black", fg='white')
        self.lbl_1.place(x=50, y=30)

        self.customer_button = Button(self.root, text='Customer', height=2, width=10, bg="red", fg='white', command=self.open_customerBtn)
        self.customer_button.place(x=100, y=80)
        self.driver_button = Button(self.root, text='Driver', height=2, width=10, bg="red", fg='white', command=self.open_driverBtn)
        self.driver_button.place(x=200, y=80)

    def open_customerBtn(self):
        from Registration import Registration
        self.root.destroy()

        customer_window = Tk()
        register = Registration(customer_window)
        customer_window.mainloop()

    def open_driverBtn(self):
        from RegistrationDriver import RegistrationDriverForm
        self.root.destroy()

        driver_window = Tk()
        registerDriver = RegistrationDriverForm(driver_window)
        driver_window.mainloop()


if __name__ == '__main__':
    root = Tk()
    Signup(root)
    root.mainloop()
