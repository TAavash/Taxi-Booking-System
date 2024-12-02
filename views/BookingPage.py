from tkinter import *
from tkinter import messagebox

from PIL import Image as PILImage, ImageTk


class BookingPage:

    def __init__(self, root):
        self.root = root
        self.root.state('zoomed')
        self.root.title('Safe Taxi Booking')
        self.root.resizable(False, False)
        self.root.config(bg="#FBC207")

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

        self.home_button = Button(self.pnlBody, text='HOME', height=2, width=10, bg="#1f2b22", bd=0, fg='light green', command=self.home_print)
        self.home_button.place(x=500, y=40)
        self.ride_button = Button(self.pnlBody, text='BOOK A RIDE', height=2, width=10, bg="#1f2b22", bd=0, fg='light green', command=self.messaging)
        self.ride_button.place(x=600, y=40)
        self.about_button = Button(self.pnlBody, text='ABOUT US', height=2, width=10, bg="#1f2b22", bd=0, fg='light green', command=self.about_us)
        self.about_button.place(x=700, y=40)
        self.join_button = Button(self.pnlBody, text='JOIN US', height=2, width=10, bg="#1f2b22", bd=0, fg='light green', command=self.messaging)
        self.join_button.place(x=800, y=40)

        self.log_button = Button(self.pnlBody, text='Login', height=2, width=15, bg="red", fg='white', command=self.open_login)
        self.log_button.place(x=1200, y=20)
        self.sign_button = Button(self.pnlBody, text='Signup', height=2, width=15, bg="red", fg='white', command=self.open_signup)
        self.sign_button.place(x=1400, y=20)

        self.initial_state = {
            "result_label_text": "",
            "txtUsername_text": "",
            "txtPassword_text": "",
            "entry_fields_visible": True
        }

        self.result_label = Label(self.pnlBody2, text="", font=("bold", 12), bg="#FBC207")
        self.result_label.place(x=10, y=10, height=720, width=900)

    def messaging(self):
        if messagebox.askyesno(title="Error", message="Would uou like to Login in order to start booking?"):
            # self.root.destroy()
            self.open_login()

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

    def about_us(self):
        self.reset_label()
        name = "SAFE TAXI BOOKING SYSTEM"
        email = "safetaxitrip123@gmail.com"
        contact = "+977 9xxxx xxxxx"
        country = "Nepal"
        font_size = 30

        self.result_label.config(
            bg="#FBC207",
            text=f"Company Name: {name}\nEmail: {email}\nContact number: {contact}\nCountry: {country}",
            font=("Arial", font_size)  # Adjust the font family and style as needed
        )

    def reset_gui(self):
        # Reset the entire GUI to its initial state
        self.result_label.config(text=self.initial_state["result_label_text"])
        self.image3_label.place_forget()
        self.image4_label.place_forget()
        # Reset other widgets to their initial states if needed
        # Example: self.other_button.config(state=..., text=...)

    def reset_label(self):
        # Reset the label text when the "Home" button is clicked
        # self.result_label.config(text="")
        self.reset_gui()

    def open_login(self):
        from Login import Login
        self.root.destroy()

        Login_window = Tk()
        login = Login(Login_window)
        Login_window.mainloop()

    def open_signup(self):
        from Signup import Signup
        self.root.destroy()

        signup_window = Tk()
        sign = Signup(signup_window)
        signup_window.mainloop()


if __name__ == '__main__':
    root = Tk()
    BookingPage(root)
    root.mainloop()
