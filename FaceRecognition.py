from cv2 import VideoCapture
import numpy as np
import pandas as pd
import cv2
import tkinter as tk
from datetime import date
import time

from keras.models import load_model
from time import sleep
from tensorflow.keras.utils import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np


face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml"); #using this file

classifier =load_model(r'C:\Users\UserX\Desktop\Attendence_System_with_Face_Recognition\emotion_model.h5')   #using this file "emotion_model.h5" inside the '' signs path of the emotion_model.h5 should be written

emotion_labels = ['Angry','Disgust','Fear','Happy','Neutral', 'Sad', 'Surprise']    #emotion labels

masterFaceRecognitionPage = tk.Tk()

canvas = tk.Canvas(masterFaceRecognitionPage, height=450, width=750)

canvas.pack()

today = date.today()    #for finding the day
t = time.localtime()    #for finding the time


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')   #load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter, the number of persons you want to include
   
id = 4 #two persons (e.g. Ali, Veli.....)    25 students that taking the class 

names = ['','name1','name2','name3','name4']  #key in names, start from the second place, leave first empty
    
    


# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img =cam.read()

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
    )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))

            labels = []
           
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
                roi_gray = gray[y:y+h,x:x+w]
                roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)

                if np.sum([roi_gray])!=0:
                    roi = roi_gray.astype('float')/255.0
                    roi = img_to_array(roi)
                    roi = np.expand_dims(roi,axis=0)

                    prediction = classifier.predict(roi)[0]
                    label=emotion_labels[prediction.argmax()]
                    label_position = (x+5,y+h+20)
                    cv2.putText(img,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                    
                    d1 = today.strftime("%d/%m/%Y")
                    current_time = time.strftime("%H:%M:%S", t)

                    
                    df = pd.DataFrame({'Name':[id],'Time':[current_time],'Day':[d1],'Emotion':[label]})
                    df.to_excel('./AttendenceList.xlsx',index=False)
                        
                else:
                    cv2.putText(img,'No Faces',(30,80),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2)
            
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
                
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+110,y+h-60), font, 1, (255,255,0), 1)  
            
    cv2.imshow('Face Recognition & Emotion Detection Page',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break


masterFaceRecognitionPage.withdraw()
cam.release()
cv2.destroyAllWindows()


masterFaceRecognitionPage.mainloop()

