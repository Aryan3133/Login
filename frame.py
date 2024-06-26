import customtkinter as ctk
import tkinter
from functions import *

class mainframe(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master)
        #The APX
        self.master=master
        self.data=data

        self.d_frame=ctk.CTkFrame(self, fg_color="white")
        self.d_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.context_frame=ctk.CTkFrame(self.d_frame, height=725, width=500, corner_radius=50, fg_color="black")
        self.context_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.w_label=ctk.CTkLabel(self.context_frame, text="Sawagatam", font=("monotype corsiva", 50), text_color="white")
        self.w_label.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)

        self.error_label=ctk.CTkLabel(self.context_frame, text="", font=("cascadia mono", 18), text_color="red")
        self.error_label.place(relx=0.17, rely=0.35, anchor="w")

        self.u_entry=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="User_name", placeholder_text_color="black",font=("cascadia mono", 18),text_color="black", fg_color="white", corner_radius=50)
        self.u_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        self.p_entry=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="Gopya Sacho", placeholder_text_color="black",text_color="black", font=("cascadia mono", 18),fg_color="white", corner_radius=50, show="*")
        self.p_entry.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.value=ctk.BooleanVar()
        self.show_password=ctk.CTkCheckBox(self.context_frame, text="Show password", font=("cascadia mono", 14),corner_radius=30, variable=self.value, command=lambda:show_password(self.p_entry, self.value))
        self.show_password.place(relx=0.17, rely=0.58, anchor="w")

        self.forgot_password=ctk.CTkButton(self.context_frame, text="Birsiyo Password?",font=("cascadia mono", 14), corner_radius=50, text_color="white", fg_color="transparent", hover="disable", command= self.change_password)
        self.forgot_password.place(relx=0.83, rely=0.58, anchor="e")

        self.login=ctk.CTkButton(self.context_frame, height=50, width=150, text="Login",font=("cascadia mono", 18), fg_color="red", corner_radius=50, command=self.check_login_credential)
        self.login.place(relx=0.17, rely=0.7, anchor="w")

        self.sign_up=ctk.CTkButton(self.context_frame, height=50, width=150, text="Sign_up",font=("cascadia mono", 18), fg_color="red", corner_radius=50, command=self.register)
        self.sign_up.place(relx=0.83, rely=0.7, anchor="e")
    
    def change_password(self):
        self.master.Forgot_p()

    def check_login_credential(self):
        user=self.u_entry.get()
        password=self.p_entry.get()

        if not user or not password:
            error(self,"*Enter the password")

        elif not user_exists(user):
            error(self,"*No user found")
        
        elif check_credential(user, password):
            self.data['user']=user
            self.data['time']=time()
            insert_log_data(self.data)
            self.master.Login()

        else:
            error(self,"*invalid password")

    def register(self):
        
        self.master.Signup()


class loginframe(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        #The APX
        self.master=master
    
        self.configure(fg_color="white")

        self.back=ctk.CTkButton(self, text="<Back", command=lambda:back2main(self), fg_color="blue", hover_color="black", corner_radius=30)
        self.back.place(x=30, y=18)

        self.context_frame=ctk.CTkFrame(self, height=725, width=500, corner_radius=50, fg_color="black")
        self.context_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.w_label=ctk.CTkLabel(self.context_frame, text="Hello", font=("monotype corsiva", 50), text_color="white")
        self.w_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        
        self.skip=ctk.CTkButton(self.context_frame, height=50, width=300, text="continue", fg_color="red", corner_radius=50, command=self.start)
        self.skip.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
    
    def start(self):
        print("OK")

    

class forgotframe_1(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master)
        #The APX
        self.master=master
        self.data=data
    
        self.d_frame=ctk.CTkFrame(self, fg_color="white")
        self.d_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.back=ctk.CTkButton(self.d_frame, text="<Back", command=lambda:back2main(self), fg_color="blue", hover_color="black", corner_radius=30)
        self.back.place(x=30, y=18)

        self.context_frame=ctk.CTkFrame(self.d_frame, height=725, width=500, corner_radius=50, fg_color="black")
        self.context_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.info_label=ctk.CTkLabel(self.context_frame, text="Enter your Email", font=("monotype corsiva", 50), text_color="white")
        self.info_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        self.E_entry=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="E-mail",text_color="black",placeholder_text_color="black",font=("cascadia mono", 18), fg_color="white", corner_radius=50)
        self.E_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.error_label=ctk.CTkLabel(self.context_frame, text="", font=("cascadia mono", 18), text_color="red")
        self.error_label.place(relx=0.17, rely=0.55, anchor="w")

        self.send=ctk.CTkButton(self.context_frame, height=50, width=300, text="Send code", fg_color="red", corner_radius=50, command=self.send)
        self.send.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    def send(self):
            self.data['email']=self.E_entry.get()
            if not self.data['email']:
                error(self,'*Entry not filled')
            elif not email_exists(self.data['email']):
                error(self,'*User doesnot exist')
            else:
                self.data['otp']=otp_generator()
                self.subject='OTP verification'
                self.msg="The OTP is"+self.data['otp']

                send_mail(self.data['email'],self.subject, self.data['otp'])
                switch(self)

    


class forgotframe_2(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master)
        #The APX
        self.master=master
        self.data=data
    
        self.d_frame=ctk.CTkFrame(self, fg_color="white")
        self.d_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.back=ctk.CTkButton(self.d_frame, text="<Back", command=lambda:switch(self), fg_color="blue", hover_color="black", corner_radius=30)
        self.back.place(x=30, y=18)

        self.context_frame=ctk.CTkFrame(self.d_frame, height=725, width=500, corner_radius=50, fg_color="black")
        self.context_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.info_label=ctk.CTkLabel(self.context_frame, text="Enter OTP", font=("monotype corsiva", 50), text_color="white")
        self.info_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        self.E_entry=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="OTP",text_color="black",font=("cascadia mono", 18),placeholder_text_color="black", fg_color="white", corner_radius=50)
        self.E_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.error_label=ctk.CTkLabel(self.context_frame, text="", font=("cascadia mono", 18), text_color="red")
        self.error_label.place(relx=0.17, rely=0.55, anchor="w")

        self.submit=ctk.CTkButton(self.context_frame, height=50, width=300, text="Submit", fg_color="red", corner_radius=50, command=self.submit)
        self.submit.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    def submit(self):
            self.data['V_otp']=self.E_entry.get()
            if not self.data['V_otp']:
                error(self,"*enter otp")
            elif self.data['otp']!=self.data['V_otp']:
                error(self,"*OTP donot match")
            else:
                switch(self)

class forgotframe_3(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master)
        #The APX
        self.master=master
        self.data=data
    
        self.d_frame=ctk.CTkFrame(self, fg_color="white")
        self.d_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.back=ctk.CTkButton(self.d_frame, text="<Back", command=lambda:switch(self), fg_color="blue", hover_color="black", corner_radius=30)
        self.back.place(x=30, y=18)

        self.context_frame=ctk.CTkFrame(self.d_frame, height=725, width=500, corner_radius=50, fg_color="black")
        self.context_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.info_label=ctk.CTkLabel(self.context_frame, text="Enter new_password", font=("monotype corsiva", 50), text_color="white")
        self.info_label.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

        self.P_entry=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="Password",text_color="black",placeholder_text_color="black", font=("cascadia mono", 18),fg_color="white", corner_radius=50)
        self.P_entry.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

        self.CP_entry=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="Confirm Password",text_color="black",placeholder_text_color="black",font=("cascadia mono", 18), fg_color="white", corner_radius=50)
        self.CP_entry.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

        self.error_label=ctk.CTkLabel(self.context_frame, text="", font=("cascadia mono", 18), text_color="red")
        self.error_label.place(relx=0.17, rely=0.55, anchor="w")

        self.submit=ctk.CTkButton(self.context_frame, height=50, width=300, text="Submit", fg_color="red", corner_radius=50, command=self.submit)
        self.submit.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    def submit(self):
            self.data['password']=self.P_entry.get()
            if not self.data['password'] or not self.CP_entry.get():
                error(self,'*entry not complete')
            elif self.data['password']!=self.CP_entry.get():
                error(self,*'Password donot match')
            else:
                updating_password(self.data)
                print("ok")



class signupframe_1(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master)
        #The APX
        self.master=master
        self.data=data
        
    
        self.d_frame=ctk.CTkFrame(self, fg_color="white")
        self.d_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.back=ctk.CTkButton(self.d_frame, text="<Back", command=lambda:back2main(self), fg_color="blue", hover_color="black", corner_radius=30)
        self.back.place(x=30, y=18)

        self.context_frame=ctk.CTkScrollableFrame(self.d_frame, height=625, width=500, fg_color="black", corner_radius=50)
        self.context_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.context_frame.grid_columnconfigure(0, weight=1)

        self.info_label=ctk.CTkLabel(self.context_frame, text="Enter your detail", font=("monotype corsiva", 50), text_color="white")
        self.info_label.grid(row=0, column=0, pady=(10,50))

        self.name=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="Name", placeholder_text_color="black",font=("cascadia mono", 18),text_color="black", fg_color="white", corner_radius=50)
        self.name.grid(row=1, column=0, pady=18)

        self.email=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="E-mail", placeholder_text_color="black",font=("cascadia mono", 18),text_color="black", fg_color="white", corner_radius=50)
        self.email.grid(row=2, column=0, pady=18)

        self.dob=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="DOB:YYYY/MM/DD", placeholder_text_color="black",font=("cascadia mono", 18),text_color="black", fg_color="white", corner_radius=50)
        self.dob.grid(row=3, column=0, pady=18)

        self.address=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="Address", placeholder_text_color="black",font=("cascadia mono", 18),text_color="black", fg_color="white", corner_radius=50)
        self.address.grid(row=4, column=0, pady=18)

        self.phone_no=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="Phone number", placeholder_text_color="black",font=("cascadia mono", 18),text_color="black", fg_color="white", corner_radius=50)
        self.phone_no.grid(row=5, column=0, pady=18)

        self.securityquestion_var=ctk.StringVar(value="Select Security Question")
        self.securityquestion=["What is your mother's name?", "What is the name of your first pet?", "In what city were you born?"]
        self.question=ctk.CTkComboBox(self.context_frame,height=50 , width=350,fg_color="white",variable=self.securityquestion_var,font=("cascadia mono", 16), values=self.securityquestion, text_color="black")
        self.question.grid(row=6, column=0, pady=18)
        self.answer=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="", placeholder_text_color="black",font=("cascadia mono", 18), fg_color="white",text_color="black", corner_radius=50)
        self.answer.grid(row=7, column=0, pady=18)
        self.error_label=ctk.CTkLabel(self.context_frame, text="", font=('cascadia mono', 18), text_color="red")
        self.error_label.grid(row=8, column=0, pady=0)
        
        self.continue_button=ctk.CTkButton(self.context_frame, height=50, width=150, text="Continue",text_color="black", font=("cascadia mono", 18), fg_color="red", command=self.next)
        self.continue_button.grid(row=9, column=0, pady=18)

    def next(self):
        self.data['name']=self.name.get()
        self.data['email']=self.email.get()
        self.data['dob']=self.dob.get()
        self.data['address']=self.address.get()
        self.data['phone_no']=self.phone_no.get()
        self.data['security_question']=self.securityquestion_var.get()
        self.data['answer']=self.answer.get()
        i=0
        for value in self.data.values():
            if not value:
                i=i+1

        if i>0:
            error(self,"*Answer every field")

        elif not is_valid_chars(self.data['name']):
            print("Name and Surname must contain only English letters.")
            error(self,'*Use Only English Lettes in Name')
        # Check if fields contain only English letters and standard characters

        elif self.data['security_question'] == "Select Security Question":
            error(self,'*Invalid Security Question')

        elif not is_valid_email(self.data['email']):
            error(self,"*Please enter a valid email address")
        # Call the register_user function from functions.py

        elif email_exists(self.data['email']):
            error(self,'*User already exists')

        elif not check_phoneno(self.data["phone_no"]):
            error(self,'*Enter phone Number in standard format')

        else:
            switch(self)
        
    
        
class signupframe_2(ctk.CTkFrame):
    def __init__(self, master, data):
        super().__init__(master)
        #The APX
        self.master=master
        self.data=data
    
        self.d_frame=ctk.CTkFrame(self, fg_color="white")
        self.d_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        self.back=ctk.CTkButton(self.d_frame, text="<Back", command=lambda:switch(self), fg_color="blue", hover_color="black", corner_radius=30)
        self.back.place(x=30, y=18)

        self.context_frame=ctk.CTkScrollableFrame(self.d_frame, height=625, width=500, fg_color="black", corner_radius=50)
        self.context_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.context_frame.grid_columnconfigure(0, weight=1)

        self.info_label=ctk.CTkLabel(self.context_frame, text="Step 2", font=("monotype corsiva", 50), text_color="white")
        self.info_label.grid(row=0, column=0, pady=(10,50))

        self.user_id=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="User_name", font=("cascadia mono", 18),placeholder_text_color="black",text_color="black", fg_color="white", corner_radius=50)
        self.user_id.grid(row=1, column=0, pady=18)

        self.password=ctk.CTkEntry(self.context_frame, height=50, width=350, placeholder_text="Password",show="*", font=("cascadia mono", 18),placeholder_text_color="black",text_color="black", fg_color="white", corner_radius=50)
        self.password.grid(row=2, column=0, pady=18)

        self.confirm_password=ctk.CTkEntry(self.context_frame, height=50, width=350,font=("cascadia mono", 18), placeholder_text="Confirm_Password",show="*", placeholder_text_color="black",text_color="black", fg_color="white", corner_radius=50)
        self.confirm_password.grid(row=3, column=0, pady=(18,0))

        self.value=ctk.BooleanVar()
        self.show_password=ctk.CTkCheckBox(self.context_frame, text="Show password", font=("cascadia mono", 14),corner_radius=30, variable=self.value, command=self.show_password)
        self.show_password.grid(row=4, column=0, padx=80, pady=(10,18), sticky= 'w')

        self.error_label=ctk.CTkLabel(self.context_frame, text="", font=('cascadia mono', 18), text_color="red")
        self.error_label.grid(row=5, column=0, pady=0)

        self.submit_button=ctk.CTkButton(self.context_frame, height=50, width=150, text="Submit",text_color="black", font=("cascadia mono", 18), fg_color="red", command=self.submit)
        self.submit_button.grid(row=6, column=0, pady=18)

    def show_password(self):
        if self.value.get():
            self.password.configure(show="")
            self.confirm_password.configure(show="")

        else:
            self.password.configure(show="*") 
            self.confirm_password.configure(show="*")


    def submit(self):
        self.data['user_name']=self.user_id.get()
        self.data['password']=self.password.get()

        if not self.data['user_name'] or not self.data['password'] or not self.confirm_password.get():
            error(self,"*Complete all field")
        elif self.data['password']!=self.confirm_password.get():
            error(self,"*Password donot match")
        elif user_exists(self.data['user_name']):
            error(self,"*User name already in use create a different one")
        else:
            self.data['time']=time()
            insert_reg_data(self.data)
            back2main(self)

