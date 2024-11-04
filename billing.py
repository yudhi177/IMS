from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk,messagebox

class billClass:
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
            # Add a default image or label here

        title = Label(self.root, text="Inventory Management System", font=("times new roman", 40, "bold"), bg="#010c48", fg="white", anchor="w", padx=20, image=self.icon_title, compound=LEFT).place(x=0, y=0, relwidth=1, height=70)

        # ===btn_logout===
        btn_logout = Button(self.root, text="Logout", font=("times new roman", 15, "bold"), bg="yellow", cursor="hand2").place(x=1150, y=10, height=50, width=150)

        # ===clock===
        self.lbl_clock = Label(self.root, text="welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time:HH:MM:SS ", font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=6, y=70, relwidth=1, height=30)

        # =========product frame====================
        self.var_search=StringVar()
        
        productFrame1 = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        productFrame1.place(x=10, y=110, width=410, height=550)
        
        ptitle = Label(productFrame1, text="All Products", font=("goudy old style", 20, "bold"), bg="#262626", fg="white").pack(side=TOP, fill=X)

        # =========product Search frame====================
        
        productFrame2 = Frame(productFrame1, bd=2, relief=RIDGE, bg="white")
        productFrame2.place(x=2, y=42, width=398, height=90)

        search_search = Label(productFrame2, text="Search Product ", font=("times new roman", 15, "bold"), bg="white", fg="green").place(x=2,y=5)
        lbl_search=Label(productFrame2,text="Product Name", font=("times new roman", 15, "bold"), bg="white").place(x=1,y=45)
        txt_search=Entry(productFrame2,textvariable=self.var_search ,font=("times new roman", 15), bg="lightyellow").place(x=128,y=47,width=150,height=22)
        
        btn_search=Button(productFrame2, text="Search", font=("goudy old style",15), bg="#2196f3", fg="white",cursor="hand2").place(x=285,y=45,width=100,height=25)
        btn_show_all=Button(productFrame2, text="Show All", font=("goudy old style",15), bg="#083531", fg="white",cursor="hand2").place(x=285,y=10,width=100,height=25)
        
        # =========product Details frame====================
        ProductFrame3 = Frame(productFrame1, bd=3, relief=RIDGE)
        ProductFrame3.place(x=2, y=140, width=395, height=375)

        scrolly = Scrollbar(ProductFrame3, orient=VERTICAL)
        scrollx = Scrollbar(ProductFrame3, orient=HORIZONTAL)

        self.product_table = ttk.Treeview(ProductFrame3, columns=("pid", "name", "price", "qty","status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.product_table.xview)
        scrolly.config(command=self.product_table.yview)

        self.product_table.heading("pid", text="PID")
        self.product_table.heading("name", text="Name")
        self.product_table.heading("price", text="Price")
        self.product_table.heading("qty", text="QTY")
        self.product_table.heading("status", text="Status")
        self.product_table["show"] = "headings"

        self.product_table.column("pid", width=90)
        self.product_table.column("name", width=100)
        self.product_table.column("price", width=100)
        self.product_table.column("qty", width=100)
        self.product_table.column("status", width=100)
        self.product_table.pack(fill=BOTH, expand=1)
        #self.product_table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=Label(productFrame1,text="Note:'Enter 0 Quantity to remove product fron your Cart'",font=("goudy old style",12),anchor='w',bg="white",fg="red").pack(side=BOTTOM, fill=X)
        
        #CustomerFrame
        self.var_cname=StringVar()
        self.var_contact=StringVar()
        CustomerFrame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        CustomerFrame.place(x=420, y=110, width=530, height=70)
        ctitle = Label(CustomerFrame, text="Customer Details", font=("goudy old style", 15), bg="lightgrey").pack(side=TOP, fill=X)
        lbl_name=Label(CustomerFrame,text="Name", font=("times new roman", 15), bg="white").place(x=5,y=35)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname ,font=("times new roman", 13), bg="lightyellow").place(x=80,y=35,width=180)
        
        lbl_contact=Label(CustomerFrame,text="Contact No.", font=("times new roman", 15), bg="white").place(x=270,y=35)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact ,font=("times new roman", 13), bg="lightyellow").place(x=380,y=35,width=140)
        
        
        #======CAL CART FRAME=============
        Cal_Cart_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Cal_Cart_Frame.place(x=420, y=190, width=530, height=360)
        
        
        #======CALCULATOR FRAME=============
        self.var_cal_input=StringVar()
        
        Cal_Frame = Frame(Cal_Cart_Frame, bd=11, relief=RIDGE, bg="white")
        Cal_Frame.place(x=5, y=10, width=268, height=340)
        
        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=("arial",15,"bold"),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        
        btn_7=Button(Cal_Frame,text='7',font=("arial",15,"bold"),command=lambda:self.get_input(7),cursor="hand2",bd=5,width=4,pady=12).grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=("arial",15,"bold"),command=lambda:self.get_input(8),cursor="hand2",bd=5,width=4,pady=12).grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=("arial",15,"bold"),command=lambda:self.get_input(9),cursor="hand2",bd=5,width=4,pady=12).grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=("arial",15,"bold"),command=lambda:self.get_input('+'),cursor="hand2",bd=5,width=4,pady=12).grid(row=1,column=3)
        
        btn_4=Button(Cal_Frame,text='4',font=("arial",15,"bold"),command=lambda:self.get_input(4),cursor="hand2",bd=5,width=4,pady=12).grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=("arial",15,"bold"),command=lambda:self.get_input(5),cursor="hand2",bd=5,width=4,pady=12).grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=("arial",15,"bold"),command=lambda:self.get_input(6),cursor="hand2",bd=5,width=4,pady=12).grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text='-',font=("arial",15,"bold"),command=lambda:self.get_input('-'),cursor="hand2",bd=5,width=4,pady=12).grid(row=2,column=3)
        
        btn_1=Button(Cal_Frame,text='1',font=("arial",15,"bold"),command=lambda:self.get_input(1),cursor="hand2",bd=5,width=4,pady=12).grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=("arial",15,"bold"),command=lambda:self.get_input(2),cursor="hand2",bd=5,width=4,pady=12).grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text='3',font=("arial",15,"bold"),command=lambda:self.get_input(3),cursor="hand2",bd=5,width=4,pady=12).grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text='*',font=("arial",15,"bold"),command=lambda:self.get_input('*'),cursor="hand2",bd=5,width=4,pady=12).grid(row=3,column=3)
        
        btn_0=Button(Cal_Frame,text='0',font=("arial",15,"bold"),command=lambda:self.get_input(0),cursor="hand2",bd=5,width=4,pady=15).grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='c',font=("arial",15,"bold"),command=self.clear_cal,cursor="hand2",bd=5,width=4,pady=15).grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',font=("arial",15,"bold"),command=self.perform_cal,cursor="hand2",bd=5,width=4,pady=15).grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=("arial",15,"bold"),command=lambda:self.get_input('/'),cursor="hand2",bd=5,width=4,pady=15).grid(row=4,column=3)
        
                       
        #======CART FRAME=============
        Cart_Frame = Frame(Cal_Cart_Frame, bd=3, relief=RIDGE)
        Cart_Frame.place(x=280, y=8, width=245, height=342)
        cartTitle = Label(Cart_Frame, text="Cart \t Total Product: [0]", font=("goudy old style", 15), bg="lightgrey").pack(side=TOP, fill=X)
        
        scrolly = Scrollbar(Cart_Frame, orient=VERTICAL)
        scrollx = Scrollbar(Cart_Frame, orient=HORIZONTAL)

        self.cartTable = ttk.Treeview(Cart_Frame, columns=("pid", "name", "price", "qty","status"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.cartTable.xview)
        scrolly.config(command=self.cartTable.yview)

        self.cartTable.heading("pid", text="PID")
        self.cartTable.heading("name", text="Name")
        self.cartTable.heading("price", text="Price")
        self.cartTable.heading("qty", text="QTY")
        self.cartTable.heading("status", text="Status")
        self.cartTable["show"] = "headings"

        self.cartTable.column("pid", width=40)
        self.cartTable.column("name", width=100)
        self.cartTable.column("price", width=90)
        self.cartTable.column("qty", width=40)
        self.cartTable.column("status", width=90)
        self.cartTable.pack(fill=BOTH, expand=1)
        #self.cartTable.bind("<ButtonRelease-1>",self.get_data)
        
        #=========ADD CART WIDGETS FRAME=============
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()
        Add_CartWidgets_Frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        Add_CartWidgets_Frame.place(x=420, y=550, width=530, height=110)
        
        lb1_p_name = Label(Add_CartWidgets_Frame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_p_name = Entry(Add_CartWidgets_Frame,textvariable=self.var_pname,font=("times new roman",15),bg="light yellow",state='readonly').place(x=5,y=35,width=190,height=22)
        
        lb1_p_price = Label(Add_CartWidgets_Frame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_p_price = Entry(Add_CartWidgets_Frame,textvariable=self.var_price,font=("times new roman",15),bg="light yellow",state='readonly').place(x=230,y=35,width=150,height=22)
        
        lb1_p_qty = Label(Add_CartWidgets_Frame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_p_qty = Entry(Add_CartWidgets_Frame,textvariable=self.var_qty,font=("times new roman",15),bg="light yellow").place(x=390,y=35,width=120,height=22)
        
        self.lb1_inStock = Label(Add_CartWidgets_Frame,text="In Stock [999]",font=("times new roman",15),bg="white")
        self.lb1_inStock.place(x=5,y=70)
        
        btn_clear_cart = Button(Add_CartWidgets_Frame,text="Clear",font=("times new roman",15,"bold"),bg="lightgrey",cursor="hand2").place(x=180,y=70,width=170,height=30)
        btn_add_cart = Button(Add_CartWidgets_Frame,text="Add | Update Cart",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=340,y=70,width=180,height=30)
        
        #===========BILLING AREA =================
        billFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billFrame.place(x=953,y=110,width=410,height=410)
        
        bTitle = Label(billFrame, text="Customer Bill Area", font=("goudy old style", 20, "bold"), bg="#262626", fg="white").pack(side=TOP, fill=X)
        scrolly=Scrollbar(billFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)
        
        self.txt_bill_area=Text(billFrame,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        
        #================BILLING BUTTONS==============
        billMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        billMenuFrame.place(x=953,y=520,width=410,height=140)
        
        self.lb1_amnt=Label(billMenuFrame,text='Bill Amount\n[0]', font=("goudy old style",15,"bold"),bg="#3f51b5",fg="white")
        self.lb1_amnt.place(x=2,y=5,width=120,height=70)
        
        self.lb1_discount=Label(billMenuFrame,text='Discount\n[5%]', font=("goudy old style",15,"bold"),bg="#8bc34a",fg="white")
        self.lb1_discount.place(x=124,y=5,width=120,height=70)
        
        self.lb1_net_pay=Label(billMenuFrame,text='Net Pay\n[0]', font=("goudy old style",15,"bold"),bg="#607d8b",fg="white")
        self.lb1_net_pay.place(x=246,y=5,width=160,height=70)
        
        btn_print=Button(billMenuFrame,text='Print',cursor="hand2", font=("goudy old style",15,"bold"),bg="light green",fg="white")
        btn_print.place(x=2,y=80,width=120,height=50)
        
        btn_clear_all=Button(billMenuFrame,text='Clear All',cursor="hand2", font=("goudy old style",15,"bold"),bg="grey",fg="white")
        btn_clear_all.place(x=124,y=80,width=120,height=70)
        
        btn_generate=Button(billMenuFrame,text='Generate Bill',cursor="hand2", font=("goudy old style",15,"bold"),bg="#009688",fg="white")
        btn_generate.place(x=246,y=80,width=160,height=70)
        
        #==============footer=======================
        footer=Label(self.root,text="IMS-Inventory Management System | Developed BY Group 6\nFor Any Techbical Issue Contact: 8930xxxxxx",font=("times new roman",11),bg="#4d636d",fg="white",bd=0,cursor="hand2").pack(side=BOTTOM,fill=X)
        
        
        
#=================ALL FUNCTIONS===================
    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)        
    
    def clear_cal(self):
        self.var_cal_input.set('')
        
    def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))   
        
if __name__ == "__main__":
    root = Tk()
    obj = billClass(root)
    root.mainloop()