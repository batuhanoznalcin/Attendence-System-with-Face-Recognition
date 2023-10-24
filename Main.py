import tkinter as tk


master = tk.Tk()
canvas = tk.Canvas(master, height=450, width=750, bg='blue')
master.title("Main Page")   #the title of the tk form
canvas.pack()

def Login_Page():   #function that makes disappear this page and redirects to the LoginPage
    master.withdraw()
    import LoginPage
    
def Register_Page():
    master.withdraw()   #function that makes disappear this page and redirects to the LoginPage
    import RegisterPage
    
loginButton = tk.Button(master, text="Login", fg='white', command=Login_Page, bg='red', height=5, width=8)  #fg = fontcolor bg=backgroundcolor creating button 
loginButton.place(x=300, y=190) #placing button

registerButton = tk.Button(master, text="Register",fg='white', command=Register_Page, bg='red', height=5, width=8)  #creating button
registerButton.place(x=400, y=190)  #placing button

master.mainloop()
