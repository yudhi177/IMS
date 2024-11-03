from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3
import os

class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        
        self.var_invoice = StringVar()
        self.bill_list = []

        #===title======================
        lbl_title = Label(self.root, text="View Customer Bills", font=("goudy old style", 30), bg="#184a45", fg="white", bd=3, relief=RIDGE).pack(side=TOP, fill=X, padx=10, pady=20)
        
        lbl_invoice = Label(self.root, text="Invoice no.", font=("times new roman", 15), bg="white").place(x=50, y=100)
        txt_invoice = Entry(self.root, textvariable=self.var_invoice, font=("times new roman", 15), bg="lightyellow").place(x=160, y=100, width=180, height=28)
        
        btn_search = Button(self.root, text="Search", command=self.search, font=("times new roman", 15, "bold"), bg="#2196f3", fg="white").place(x=360, y=100, width=120, height=28)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("times new roman", 15, "bold"), bg="#f44336", fg="white").place(x=490, y=100, width=120, height=28)
        
        # Bill list
        sales_frame = Frame(self.root, bd=3, relief=RIDGE)
        sales_frame.place(x=50, y=140, width=200, height=330)
        
        scrolly = Scrollbar(sales_frame, orient=VERTICAL)
        self.Sales_list = Listbox(sales_frame, font=("goudy old style", 15), bg="white", yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.Sales_list.yview)
        self.Sales_list.pack(fill=BOTH, expand=1)
        self.Sales_list.bind("<ButtonRelease-1>", self.get_data)
        
        # List area
        bill_frame = Frame(self.root, bd=3, relief=RIDGE)
        bill_frame.place(x=280, y=140, width=410, height=330)
        
        lbl_title2 = Label(bill_frame, text="Customer Bill Area", font=("goudy old style", 20), bg="orange").pack(side=TOP, fill=X)
        
        scrolly2 = Scrollbar(bill_frame, orient=VERTICAL)
        self.area_list = Text(bill_frame, font=("goudy old style", 15), bg="lightyellow", yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.area_list.yview)
        self.area_list.pack(fill=BOTH, expand=1)
        
        # Image
        try:
            image_path = "image/cat3.jpg"  
            self.bill_photo = Image.open(image_path)
            self.bill_photo = self.bill_photo.resize((450, 300), Image.LANCZOS)
            self.bill_photo = ImageTk.PhotoImage(self.bill_photo)
        except FileNotFoundError:
            print("Error: Image file not found:", image_path)
            self.bill_photo = None
            
        if self.bill_photo:
            lbl_image = Label(self.root, image=self.bill_photo, bd=0)
            lbl_image.place(x=700, y=110)
        
        self.show()
        self.Sales_list.bind("<Double-1>", self.get_data)
    
    def show(self):
        del self.bill_list[:]
        self.Sales_list.delete(0, END)
        directory = 'bill'
        if os.path.exists(directory) and os.path.isdir(directory):
            for i in os.listdir(directory):
                if i.split('.')[-1] == 'txt':
                    print("Found file:", i)  # Debug print statement
                    self.Sales_list.insert(END, i)
                    try:
                        invoice_number = i.split('.')[0]  # Extract the invoice number from the filename
                        self.bill_list.append(invoice_number)
                    except IndexError:
                        print(f"Skipping file: {i}, not enough data after split")
        else:
            print("Directory 'bill' does not exist or is not a directory")
                
    def get_data(self, event):
        index = self.Sales_list.curselection()
        if index:
            file_name = self.Sales_list.get(index)
            self.area_list.delete('1.0', END)
            with open(f'bill/{file_name}', 'r') as f:
                self.area_list.insert(END, f.read())
            print(file_name)
    
    def search(self):       
        if self.var_invoice.get() == "":
            messagebox.showerror("Error", "Invoice no. should be required", parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                print("Invoice found:", self.var_invoice.get())
                with open(f'bill/{self.var_invoice.get()}.txt', 'r') as fp:
                    self.area_list.delete('1.0', END)
                    for i in fp:
                        self.area_list.insert(END, i)
            else:
                messagebox.showerror("Error", "Invoice no. not found", parent=self.root)
    
    def clear(self):
        self.var_invoice.set("")
        self.area_list.delete('1.0', END)

if __name__ == "__main__":
    root = Tk()
    obj = salesClass(root)
    root.mainloop()
