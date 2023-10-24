import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

masterRegisteration = tk.Tk()
canvas = tk.Canvas(masterRegisteration, height=450, width=750, bg="green")
masterRegisteration.title("Registeration Page")
canvas.pack()

lastname = tk.StringVar()
firstname = tk.StringVar()
department = tk.StringVar()
username = tk.StringVar() 
password = tk.StringVar()

def RegisterationAction():
    lastname = LastName_Entry.get()
    firstname = FirstName_Entry.get()
    department = Department_Entry.get()
    username = UserName_Entry.get()
    password = Password_Entry.get()
    if lastname == "" or firstname == "" or department =="" or username == "" or password =="" :
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
                MySql = ("INSERT IGNORE INTO Advisors (`LastName`, `FirstName`, `Department`, `Username`, `Password`) VALUES(%s,%s,%s,%s,%s)") #inserting without duplicate
                data = (lastname,firstname,department,username,password)
                cursor.execute(MySql,data)
                connection.commit()
                masterRegisteration.withdraw()
                import LoginPage                                       
        except Error as e:
            print("Error while connecting to MySQL", e) 
       
       


LastNameLabel = tk.Label(masterRegisteration, text="Lastname" , bg="black", fg="white")
LastNameLabel.place(x=280, y=150)
LastName_Entry = tk.Entry(masterRegisteration, textvariable=lastname, borderwidth=2)
LastName_Entry.place(x=360, y=150)

FirstNameLabel = tk.Label(masterRegisteration, text="Firstname", bg="black", fg="white")
FirstNameLabel.place(x=280, y=175)
FirstName_Entry = tk.Entry(masterRegisteration, textvariable=firstname, borderwidth=2)
FirstName_Entry.place(x=360, y=175)

DepartmentLabel = tk.Label(masterRegisteration, text="Department", bg="black", fg="white")
DepartmentLabel.place(x=275, y=200)
Department_Entry = tk.Entry(masterRegisteration,textvariable=department, borderwidth=2)
Department_Entry.place(x=360, y=200)

UserNameLabel = tk.Label(masterRegisteration, text="Username", bg="black", fg="white")
UserNameLabel.place(x=280, y=225)
UserName_Entry = tk.Entry(masterRegisteration, textvariable=username, borderwidth=2)
UserName_Entry.place(x=360, y=225)

PasswordLabel = tk.Label(masterRegisteration, text="Password", bg="black", fg="white")
PasswordLabel.place(x=280, y=250)
Password_Entry = tk.Entry(masterRegisteration, textvariable=password, borderwidth=2)
Password_Entry.place(x=360, y=250)

SubmitButton = tk.Button(masterRegisteration, text="Submit", command=RegisterationAction, height=5, width=8, bg="black" , fg="white")
SubmitButton.place(x=500, y=166)

masterRegisteration.mainloop()