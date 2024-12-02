from tkinter import *
from tkinter import messagebox
from Model.CustomerModel import CustomerModel
from Controller.CustomerController import register

from PIL import Image as PILImage, ImageTk


class Registration:
    def __init__(self,root):
        self.root = root
        self.root.geometry("700x600")
        self.root.title('Registration form')
        self.root.resizable(False, False)

        self.logo_path = r"C:\Users\AAVASH\PycharmProjects\pythonProject\TaxiAssignment\images\Logo.png"
        self.logo = PhotoImage(file=self.logo_path)
        self.root.iconphoto(True, self.logo)

        self.image = ImageTk.PhotoImage(PILImage.open("../images/22.png"))

        self.image_label = Label(image=self.image, bg="white")
        self.image_label.image = self.image
        self.image_label.place(x=0, y=0)

        self.lbl_0 = Label(self.root, text="Customer Registration Form", width=22, font=("Times New Roman", 20), bg="white")
        self.lbl_0.place(x=30, y=60)

        self.lbl_1 = Label(self.root, text="FullName", width=15, font=("bold", 10), bg="white")
        self.lbl_1.place(x=30, y=130)
        self.enter_1 = Entry(self.root, bg="light gray")
        self.enter_1.place(x=220, y=130)

        self.lbl_2 = Label(self.root, text="Email", width=15, font=("bold", 10), bg="white")
        self.lbl_2.place(x=28, y=180)
        self.enter_2 = Entry(self.root, bg="light gray")
        self.enter_2.place(x=220, y=180)

        self.lbl_3 = Label(self.root, text="Gender", width=15, font=("bold", 10), bg="white")
        self.lbl_3.place(x=30, y=230)
        self.vars = IntVar()
        Radiobutton(self.root, text="Male", padx=5, variable=self.vars, value=1, bg="white").place(x=220, y=230)
        Radiobutton(self.root, text="Female", padx=20, variable=self.vars, value=2, bg="white").place(x=280, y=230)

        self.lbl_4 = Label(self.root, text="Phone Number", width=15, font=('bold', 10), bg="white")
        self.lbl_4.place(x=40, y=280)
        self.enter_3 = Entry(self.root, bg="light gray")
        self.enter_3.place(x=220, y=280)

        self.lbl_5 = Label(self.root, text="Address", width=15, font=("bold", 10), bg="white")
        self.lbl_5.place(x=30, y=330)
        self.list_of_city = ['Kathmandu', 'Lalitpur', 'Bhaktapur', 'Chitwan', 'Gorkha', 'Others']
        self.cv = StringVar()
        self.drplist = OptionMenu(self.root, self.cv, *self.list_of_city)
        self.drplist.config(width=15, bg="white")
        self.cv.set('Select your City')
        self.drplist.place(x=220, y=330)

        self.lbl_6 = Label(self.root, text="Password", width=15, font=('bold', 10), bg="white")
        self.lbl_6.place(x=35, y=380)
        self.enter_4 = Entry(self.root, bg="light gray")
        self.enter_4.place(x=220, y=380)
        self.enter_4.config(show="*")

        self.submit_button = Button(self.root, text='Submit', width=15, bg="#3366FF", fg='white', command=self.submit)
        self.submit_button.place(x=100, y=430)
        self.back_button = Button(self.root, text='Back', width=15, bg="light gray", command=self.back)
        self.back_button.place(x=250, y=430)

        self.result_label = Label(self.root, text="", font=("bold", 12), bg="white")
        self.result_label.place(x=100, y=480)

    def open_login(self):
        from Login import Login
        self.root.destroy()

        Login_window = Tk()
        login = Login(Login_window)
        Login_window.mainloop()

    def submit(self):
        full_name = self.enter_1.get()
        email = self.enter_2.get()
        gender = "Male" if self.vars.get() == 1 else "Female"
        address = self.cv.get()
        phone = self.enter_3.get()
        password = self.enter_4.get()

        customer = CustomerModel(name=full_name, email=email, gender=gender, address=address, phone_number=phone, password=password)
        registered = register(customer)
        if registered:
            messagebox.showinfo("Registered", "Registered Successfully")

    def back(self):
        if messagebox.askyesno(title="Back To Login Page", message="Are you sure you want to go back ?"):
            self.open_login()


if __name__ == "__main__":
    customer_window = Tk()
    Registration(customer_window)
    customer_window.mainloop()
