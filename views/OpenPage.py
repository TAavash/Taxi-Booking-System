from tkinter import *
from PIL import Image as PILImage, ImageTk


class OpenPage:

    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+100+50")
        self.root.title('Safe Taxi Booking')
        self.root.resizable(False, False)
        self.root.config(bg="black")

        self.logo = ImageTk.PhotoImage(PILImage.open("../images/Logo.png"))
        self.root.iconphoto(True, self.logo)

        self.whole_image = ImageTk.PhotoImage(PILImage.open("../images/FrontPage.png"))

        self.image_label = Label(image=self.whole_image, bg="#404040")
        self.image_label.image = self.whole_image
        self.image_label.place(x=0, y=0)

        self.booking_button = Button(self.root, text='Book Trip', height=2, width=15, bg="red", fg='white', command=self.open_booking)
        self.booking_button.place(x=1200, y=20)

    def open_booking(self):
        from BookingPage import BookingPage
        self.root.destroy()

        bookingn_window = Tk()
        bookingPage = BookingPage(bookingn_window)
        bookingn_window.mainloop()


if __name__ == '__main__':
    root = Tk()
    OpenPage(root)
    root.mainloop()
