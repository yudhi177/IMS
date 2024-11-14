from tkinter import *
from tkinter import messagebox
import _sqlite3
import os


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
        
        #===== Login Frame =====
        self.employee_id = StringVar()
        self.password = StringVar()
        
        login_frame = Frame(self.root, bd=2, relief=RIDGE, background="white")
        login_frame.place(x=650, y=120, width=300, height=400)

        title = Label(login_frame, text="Login System", font=("Elephant", 30, "bold"), background="white").place(x=1, y=30, relwidth=1)
        lbl_user = Label(login_frame, text="Employee ID", font=("Andalus", 15), background="white", fg="#767171").place(x=50, y=100)
        
        
        txt_employee_id = Entry(login_frame, textvariable=self.employee_id, font=("times new roman", 15), background="#ECECEC").place(x=45, y=140, width=220)

        lbl_password = Label(login_frame, text="Password", font=("Andalus", 15), background="white", fg="#767171").place(x=50, y=180)
        txt_password = Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 15), background="#ECECEC").place(x=45, y=220, width=220)

        btn_login = Button(login_frame, command=self.login, text="Log In", font=("Arial Rounded MT bold", 15), background="#00B0F0", activebackground="#00B0F0", fg="white", activeforeground="white", cursor="hand2").place(x=45, y=280, width=220, height=35)

        hr_label = Label(login_frame, bg="lightgray").place(x=50, y=340, width=200, height=2)
        or_ = Label(login_frame, text="OR", bg="white", fg="lightgray", font=("times new roman", 15)).place(x=130, y=330)

        forget_btn = Button(login_frame, text="Forget password?",command=self.forget_window, font=("times new roman", 13), bg="white", fg="#00759E", activebackground="white", activeforeground="#00759E", bd=0).place(x=85, y=360)

        #===== Register Frame =====
        register_frame = Frame(self.root, bd=2, relief=RIDGE, background="white")
        register_frame.place(x=650, y=540, width=300, height=60)

        lbl_register = Label(register_frame, text="Don't have an account?", font=("times new roman", 13), bg="white").place(x=50, y=15)
        btn_sign_up = Button(register_frame, text="Sign up", font=("times new roman", 13, "bold"), background="white", activebackground="white", fg="#00759E", activeforeground="#00759E", bd=0).place(x=210, y=12)

        #======= Animation ========
        self.images = [
            PhotoImage(file="C:/Users/User/OneDrive/Desktop/L/Login.png").subsample(2, 2),
            PhotoImage(file="C:/Users/User/OneDrive/Desktop/L/p.png").subsample(2, 2),
            PhotoImage(file="C:/Users/User/OneDrive/Desktop/L/o.png").subsample(2, 2)
        ]
        self.current_image_index = 0
        
        # Label to display animated images
        self.lbl_animation = Label(self.root, image=self.images[self.current_image_index], background="grey", bd=0)
        self.lbl_animation.place(x=350, y=190)

        # Start the animation
        self.update_image()

    def update_image(self):
        """Function to update the image in animation."""
        self.current_image_index = (self.current_image_index + 1) % len(self.images)
        self.lbl_animation.config(image=self.images[self.current_image_index])
        
        # Call this function again after 1000ms (1 second)
        self.root.after(1000, self.update_image)

    def login(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.employee_id.get()=="" or self.password.get()=="":
                messagebox.showerror('Error','All feilds are required',parent=self.root)
                
            else:
                cur.execute("select utype from employee where eid=? and pass=?",(self.employee_id.get(),self.password.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror('Error','Invalid Username/Password',parent=self.root)
                else: 
                    
                    if user[0]=="Admin":
                        self.root.destroy()
                        os.system("python dashboard.py")
                    else:
                        self.root.destroy()
                        os.system("python billing.py")
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close() 
    def forget_window(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.employee_id.get()=="":
                messagebox.showerror('Error',"Employee ID must be required",parent=self.root)
            else:
                cur.execute("select email from employee where eid=?",(self.employee_id.get()))
                user=cur.fetchone()
                if user==None:
                    messagebox.showerror('Error','Invalid Employee ID,try again',parent=self.root)
                else: 
                    #forget window================================
                    self.var_otp=StringVar()
                    self.var_new_pass=StringVar()
                    self.var_conf_pass=StringVar()
                    #call send email funcction()
                    self.forget_win=Toplevel(self.root)
                    self.forget_win.title('Reset Password')
                    self.forget_win.geometry('400x350+500+100')
                    self.forget_win.focus_force()
                    
                    title=Label(self.forget_win,text='Reset Password',font=('goudy old style',15,'bold'),bg="#3f51b5",fg='white').pack(side=TOP,fill=X)
                    lbl_reset=Label(self.forget_win,text="Enter OTP sent on Registered Email",font=("times new roman",15)).place(x=20,y=60)
                    txt_reset=Entry(self.forget_win,textvariable=self.var_otp,font=("times new roman",15),bg="lightyellow").place(x=20,y=100,width=250,height=30)
                    btn_reset=Button(self.forget_win,text='SUBMIT',font=("times new roman",15),bg="lightblue")
                    btn_reset.place(x=280,y=100,width=100,height=30)
                    
                    lbl_new_pass=Label(self.forget_win,text="New Password",font=("times new roman",15)).place(x=20,y=160)
                    txt_new_pass=Entry(self.forget_win,textvariable=self.var_new_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=190,width=250,height=30)
                    
                    lbl_c_pass=Label(self.forget_win,text="Confirm Password",font=("times new roman",15)).place(x=20,y=225)
                    txt_c_pass=Entry(self.forget_win,textvariable=self.var_conf_pass,font=("times new roman",15),bg="lightyellow").place(x=20,y=255,width=250,height=30)
                    
                    self.btn_update=Button(self.forget_win,text='Update',state=DISABLED,font=("times new roman",15),bg="lightblue")
                    btn_reset.place(x=150,y=300,width=100,height=30)
                    
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close() 
            
            
            
            
# Main loop to run the program
if __name__ == "__main__":
    root = Tk()
    obj = LoginSystem(root)
    root.mainloop()
