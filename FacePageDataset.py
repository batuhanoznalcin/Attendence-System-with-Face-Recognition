import tkinter as tk
from tkinter import messagebox
import cv2
import sys
import os

masterFacePageDataset = tk.Tk()
canvas = tk.Canvas(masterFacePageDataset, height=450, width=750, bg="pink")
masterFacePageDataset.title("Dataset Creation Page")
canvas.pack()

idstudent = tk.StringVar()



IDLabel = tk.Label(masterFacePageDataset, text="Enter id", bg="light blue")
IDLabel.place(x=300, y=225)
ID_Entry = tk.Entry(masterFacePageDataset, textvariable = idstudent, borderwidth=2)
ID_Entry.place(x=360, y=225)

idstudent = ID_Entry.get()


def SubmitActionCreateDataset():
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height

#make sure 'haarcascade_frontalface_default.xml' is in the same folder as this code
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id (must enter number start from 1, this is the lable of person 1)





# Initialize individual sampling face count
    count = 0

#start detect your face and take 30 pictures
    while(True):

        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
            count += 1

        # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(int(ID_Entry.get())) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30: # Take 30 face sample and stop video
         break

# Do a bit of cleanup
    print("\n [INFO] Exiting Program and cleanup stuff")
    import FacePageTraining
    cam.release()
    cv2.destroyAllWindows()
    masterFacePageDataset.mainloop()


SubmitButton = tk.Button(masterFacePageDataset, text="Submit", command=SubmitActionCreateDataset,bg="light blue")
SubmitButton.place(x=500, y=223)


if idstudent.isdigit():
    dist = int(float(idstudent))
    while(dist > 0):
        SubmitActionCreateDataset()








masterFacePageDataset.mainloop()


