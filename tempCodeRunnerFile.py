def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Employee Name is required", parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!= None:
                    messagebox.showerror("Error","This Employee ID already assigned,try different",parent=self.root)
                else:
                    cur.execute("INSERT INTO employee (name, email, gender, contact, dob, doj, pass, utype, address, salary) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_address.get("1.0", END),
                        self.var_salary.get(),
                ))
                con.commit()
                messagebox.showinfo("Success", "Employee added successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()