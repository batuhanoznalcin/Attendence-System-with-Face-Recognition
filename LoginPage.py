import tkinter as tk
from tkinter import messagebox
import mysql.connector

from mysql.connector import Error

masterLogin = tk.Tk()
canvas = tk.Canvas(masterLogin, height=450, width=750, bg='light blue')

masterLogin.title("Login Page") #the title of the tk form
canvas.pack()

username = tk.StringVar()   #variable for username
password = tk.StringVar()   #variable for password

UserNameLabel = tk.Label(masterLogin, text="Username", bg="purple", fg="white") #creating label
UserNameLabel.place(x=300, y=225)   #placing label
UserName_Entry = tk.Entry(masterLogin, textvariable=username, borderwidth=2)    #creating textfield
UserName_Entry.place(x=360, y=225)  #placing textfield

PasswordLabel = tk.Label(masterLogin, text="Password", bg="purple", fg="white") #creating label
PasswordLabel.place(x=300, y=250)   #placing label
Password_Entry = tk.Entry(masterLogin, textvariable=password, show="*" , borderwidth=2) #creating textfield
Password_Entry.place(x=360, y=250)   #placing textfield

def SubmitAction(): #function that takes values form textfeilds as variables to compare with SQL database.

    username = UserName_Entry.get()
    password = Password_Entry.get()

    print(f"The name entered by you is [{username} , {password}]") #printing them to terminal

    if username == "" or password =="": #if the fields are empty messeagebox comes up to screen
        messagebox.showerror("Error","All fields are requried")
    else:
        try:    #we are doing connection
            connection = mysql.connector.connect(host='localhost',
                                                database='advisor',
                                                user='root',
                                                password='parola')
            if connection.is_connected():
                db_Info = connection.get_server_info()
                print("Connected to MySQL Server version ", db_Info)    #if connection is done this message is shown on terminal
                cursor = connection.cursor()
                cursor.execute("select * from Advisors where username =%s and password=%s",(username,password)) #SQL query
                record = cursor.fetchone()
                #print("You're connected to database with :", record)
                if record == None:
                    messagebox.showerror("Error","Invalid username & password.")#if the variables that user entered do not match with the SQL databases values this message shown
                else:
                    messagebox.showerror("Information","Welcome!")  #if they are matched this message shown
                    masterLogin.withdraw()  #if login part is over this page is disappear and DecidePage is coming
                    import DecidePage   
                    
        except Error as e:
            print("Error while connecting to MySQL", e)

def BackAction():   #if user clicks back button program goes to Main page.
    masterLogin.withdraw()
    import Main

BackButton = tk.Button(masterLogin, text="Back", command=BackAction, bg="red", fg="white", width=4)#creating button
BackButton.place(x=710, y=420)  #placing button

SubmitButton = tk.Button(masterLogin, text="Submit", command=SubmitAction, height=2, width=6, bg="orange", fg="white")#creating button
SubmitButton.place(x=500, y=227)#placing button

masterLogin.mainloop()