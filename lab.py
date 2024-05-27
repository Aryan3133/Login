import customtkinter as c
def prints():
    print(b.cget("text"))
app=c.CTk()
var=c.StringVar(value="try")
b=c.CTkRadioButton(app, text="try", command=prints)
b.pack()
d=c.CTkRadioButton(app, text="try2", command=prints)
d.pack()
app.mainloop()