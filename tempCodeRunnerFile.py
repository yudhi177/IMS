from tkinter import *
from PIL import Image, ImageTk

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")

        # ==== Title ====
        try:
            image = Image.open("image/Logo1.png")
            self.icon_title = ImageTk.PhotoImage(image)
        except FileNotFoundError:
            print("Error: Image file not found: image/Logo1.png")
        title = Label(self.root, text="Inventory Management System",
                      font=("times new roman", 40, "bold"), bg="#010c48", fg="white",
                      anchor="w", padx=20, image=self.icon_title, compound=LEFT).place(x=0, y=0, relwidth=1, height=70)

        # ===btn_logout===
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"),
                             bg="yellow", cursor="hand2").place(x=1150, y=10, height=50, width=150)

        # ===clock===
        self.lbl_clock = Label(self.root, text="welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time:HH:MM:SS ",
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)

        # ===left menu===
        try:
            image_path = "image/menu_im.png"  # Replace with the correct path
            self.MenuLogo = Image.open(image_path)
            self.MenuLogo = self.MenuLogo.resize((150, 150), Image.LANCZOS)
            self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)
        except FileNotFoundError:
            print("Error: Image file not found:", image_path)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0, y=100, width=200, height=600)

        lbl_menulogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_menulogo.pack(side=TOP, pady=20)
        
        self.icon_side=PhotoImage(file="image/side.png")
        lbl_menu=Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688").pack(side=TOP,fill=X)
        btn_employee=Button(LeftMenu, text="Employee",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman", 20,"bold"), bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
root = Tk()
obj = IMS(root)
root.mainloop()
