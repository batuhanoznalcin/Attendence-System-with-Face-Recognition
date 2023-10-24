import tkinter as tk
from tkinter import messagebox

masterDecide = tk.Tk()
canvas = tk.Canvas(masterDecide, height=450, width=750,bg="brown")

masterDecide.title("Decision Page") #the title of the tk form
canvas.pack()

def AttendenceAction(): #once the button clicks this page disappears and FaceRecognition comes.
    masterDecide.withdraw()
    import FaceRecognition


AttendenceButton = tk.Button(masterDecide, text="Click To Take Attendence", command = AttendenceAction,bg="indigo",fg="white", width=20, height=3)  #creating button
AttendenceButton.place(x=310, y=200)    #placing button



masterDecide.mainloop()

