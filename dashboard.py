from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from products import productClass
from sales import salesClass

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

        title = Label(self.root, text="Inventory Management System", font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20, image=self.icon_title, compound=LEFT).place(x=0, y=0, relwidth=1, height=70)

        # ===btn_logout===
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2").place(x=1150, y=10, height=50, width=150)

        # ===clock===
        self.lbl_clock = Label(self.root, text="welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time:HH:MM:SS ", font=("times new roman", 15), bg="#4d636d", fg="white")
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

        self.icon_side = PhotoImage(file="image/side.png")
        lbl_menu = Label(LeftMenu, text="Menu", font=("times new roman", 20), bg="#009688").pack(side=TOP, fill=X)
        btn_employee = Button(LeftMenu, text="Employee",command=self.employee,image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_supplier = Button(LeftMenu, text="Supplier",command=self.supplier, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_category = Button(LeftMenu, text="Category",command=self.category, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_product = Button(LeftMenu, text="Product",command=self.product, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = Button(LeftMenu, text="Sales",command=self.sales, image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)
        btn_exit = Button(LeftMenu, text="Exit", image=self.icon_side, compound=LEFT, padx=5, anchor="w", font=("times new roman", 20, "bold"), bg="white", bd=3, cursor="hand2").pack(side=TOP, fill=X)

        #===content===
        self.lbl_employee = Label(self.root, text="Total Employee\n[0]", bd=5, relief=RIDGE, bg="#33bbf9", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_employee.place(x=300, y=120, height=150, width=300)

        self.lbl_supplier = Label(self.root, text="Total Supplier\n[0]", bd=5, relief=RIDGE, bg="#ff5722", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=150, width=300)

        self.lbl_category = Label(self.root, text="Total Category\n[0]", bd=5, relief=RIDGE, bg="#009688", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_category.place(x=1000, y=120, height=150, width=300)

        self.lbl_product = Label(self.root, text="Total Product\n[0]", bd=5, relief=RIDGE, bg="#607D8B", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_product.place(x=300, y=300, height=150, width=300)

        self.lbl_sales = Label(self.root, text="Total Sales\n[0]", bd=5, relief=RIDGE, bg="#ffc107", fg="white", font=("goudy old style", 20, "bold"))
        self.lbl_sales.place(x=650, y=300, height=150, width=300)
        
        # ===footer===
        lbl_footer = Label(self.root, text="IMS-Inventory Management System \n for any technical issue Contact:987xxxxx00", font=("times new roman", 12), bg="#4d636d", fg="white").pack(side=BOTTOM, fill=X)
        
#==================================================================================================================================================
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
        
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
        
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)
        
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)
        
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()