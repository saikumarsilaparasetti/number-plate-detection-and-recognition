import cv2
import numpy as np
  
import pytesseract #pip install tesseract
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" #Path to the tesseract 
def OCR(img):
    #img = Image.open('img.jpg')# add Image name here with file extention
    text = pytesseract.image_to_string(img)
    print(text)
    remember = open('remember.txt','w')
    remember.write(text)
    remember.close()


#numberPlateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
plat_detector =  cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
video = cv2.VideoCapture('./test-1.MOV')

if(video.isOpened()==False):
    print('Error Reading Video')

while True:
    ret,frame = video.read()    
    gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plate = plat_detector.detectMultiScale(gray_video,scaleFactor=1.2,minNeighbors=5,minSize=(25,25))
    
    for (x,y,w,h) in plate:
        #cv2.imshow('plate',plate)
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
        #frame[y:y+h,x:x+w] = cv2.blur(frame[y:y+h,x:x+w],ksize=(10,10))
        #OCR(frame[y:y+h,x:x+w])
        cv2.imshow('plate',frame[y:y+h,x:x+w])
        cv2.putText(frame,text='License Plate',org=(x-3,y-3),fontFace=cv2.FONT_HERSHEY_COMPLEX,color=(0,0,255),thickness=1,fontScale=0.6)
        
         
    if ret == True:

        cv2.imshow('Video', frame)

        if cv2.waitKey(25) & 0xFF == ord("q"):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()            
