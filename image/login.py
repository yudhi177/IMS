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
        
        #===== Login Frame =====
        login_frame = Frame(self.root, bd=2, relief=RIDGE, background="white")
        login_frame.place(x=650, y=120, width=300, height=400)

        title = Label(login_frame, text="Login System", font=("Elephant", 30, "bold"), background="white").place(x=1, y=30, relwidth=1)
        lbl_user = Label(login_frame, text="Username", font=("Andalus", 15), background="white", fg="#767171").place(x=50, y=100)
        
        self.username = StringVar()
        self.password = StringVar()
        txt_username = Entry(login_frame, textvariable=self.username, font=("times new roman", 15), background="#ECECEC").place(x=45, y=140, width=220)

        lbl_password = Label(login_frame, text="Password", font=("Andalus", 15), background="white", fg="#767171").place(x=50, y=180)
        txt_password = Entry(login_frame, textvariable=self.password, show="*", font=("times new roman", 15), background="#ECECEC").place(x=45, y=220, width=220)

        btn_login = Button(login_frame, command=self.login, text="Log In", font=("Arial Rounded MT bold", 15), background="#00B0F0", activebackground="#00B0F0", fg="white", activeforeground="white", cursor="hand2").place(x=45, y=280, width=220, height=35)

        hr_label = Label(login_frame, bg="lightgray").place(x=50, y=340, width=200, height=2)
        or_ = Label(login_frame, text="OR", bg="white", fg="lightgray", font=("times new roman", 15)).place(x=130, y=330)

        forget_btn = Button(login_frame, text="Forget password?", font=("times new roman", 13), bg="white", fg="#00759E", activebackground="white", activeforeground="#00759E", bd=0).place(x=85, y=360)

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
        """Login function to check the credentials."""
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror("Error", "All fields are required")

        elif self.username.get() != "amit" or self.password.get() != "1234":
            messagebox.showerror("Error", "Invalid username or password\nTry again with correct credentials")

        else:
            messagebox.showinfo("Information", f"Welcome: {self.username.get()}\nYour password: {self.password.get()}")


# Main loop to run the program
if __name__ == "__main__":
    root = Tk()
    obj = LoginSystem(root)
    root.mainloop()
