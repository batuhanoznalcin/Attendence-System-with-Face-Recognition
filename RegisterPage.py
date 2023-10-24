import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

masterRegister = tk.Tk()
canvas = tk.Canvas(masterRegister, height=450, width=750,bg="crimson")
masterRegister.title("Register Page")
canvas.pack()

username = tk.StringVar() 
password = tk.StringVar()

InfoLinelabel = tk.Label(masterRegister,text='To register, person who attempts needs authority.',bg="crimson",fg="white")
InfoLinelabel.config(font=('helvetica', 14, 'underline'))
InfoLinelabel.place(x=160, y=100)

UserNameLabel = tk.Label(masterRegister, text="Username",bg="darkcyan")
UserNameLabel.place(x=258, y=225)
UserName_Entry = tk.Entry(masterRegister, textvariable=username,borderwidth=2)
UserName_Entry.place(x=320, y=225)

PasswordLabel = tk.Label(masterRegister, text="Password",bg="darkcyan")
PasswordLabel.place(x=259, y=250)
Password_Entry = tk.Entry(masterRegister, textvariable=password, show="*",borderwidth=2)
Password_Entry.place(x=320, y=250)

def RegisterAction():
    username = UserName_Entry.get()
    password = Password_Entry.get()
    print(f"The name entered by you is [{username} , {password}]")
    if username == "" or password =="":
        messagebox.showerror("Error","All fields are requried")
    else:
        try:
            connection = mysql.connector.connect(host='localhost',
                                                database='advisor',
                                                user='root',
                                                password='parola')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)
                cursor = connection.cursor()
                cursor.execute("select * from HeadOfDept where username =%s and password=%s",(username,password))
                record = cursor.fetchone()
                print("You're connected to database with :", record)
                if record == None:
                    messagebox.showerror("Error","Invalid username & password.")
                else:
                    messagebox.showerror("Error","Welcome head of Department!")
                    masterRegister.withdraw()
                    import Registeration   
                    
        except Error as e:
            print("Error while connecting to MySQL", e)

def BackAction():
    masterRegister.withdraw()
    import Main

SubmitButton = tk.Button(masterRegister, text="Submit", command=RegisterAction,bg="darkcyan")
SubmitButton.place(x=460, y=233)

BackButton = tk.Button(masterRegister, text="Back", command=BackAction, bg="darkcyan", width=4)
BackButton.place(x=710, y=420)

masterRegister.mainloop()
