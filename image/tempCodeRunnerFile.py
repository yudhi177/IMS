from tkinter import *
from tkinter import messagebox


class LoginSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")
        
        #===== Phone Image =====
        self.image_path = "C:/Users/User/OneDrive/Desktop/L/phone.png"
        self.phone_image = PhotoImage(file=self.image_path)
        self.phone_image = self.phone_image.subsample(6, 6)
        self.lbl_phone_image = Label(self.root, image=self.phone_image).place(x=200, y=90)