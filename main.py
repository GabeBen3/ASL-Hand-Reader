# USE <pip install -r requirements.txt> IN COMMAND LINE TO INSTALL ALL REQUIRED PACKAGES
# 
# Uses AI model trained with images from collectHandData.py
# Compares hand position model to predict letter signed in ASL from User
#
# We can improve the model by adding more images we capture using collectData.py
# Next steps:
    # Use random word generator to prompt for what string of ASL letters the User should attempt to input 
    # Display Graphic of the word they should input next (text & ASL representation)
    # Display letters they've gotten correct in the word so far, tell user when they've completed the word
    # Display accuracy statistics (Speed, Accuracy, etc...)
#
# Current Bugs:
    # 01: Program closes when rectangle around detected hand exits the frame from left and top side
    # 02: Problamatic Letters:
# A - Mistook with Y and J 
# B - Mistook with U
# D - R
# E - I, J
# F - J
# Z - J 
                            
import cv2
import numpy as np
import math
import time
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
from tkinter import *
from PIL import Image, ImageTk

capture = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1) #Detect Hands in capture, 1 hand
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt") #Call Model for classification

win = Tk()
win.geometry("900x600")
win.resizable(False, False)
frame_1 = Frame(win, width=900, height=600, bg="skyblue").place(x=0, y=0)
frame2 = Frame(win, width=250, height=250, bg="skyblue")
frame2.pack(side=RIGHT)
frame3 = Frame(win, width=900, height=125, bg = "skyblue")
frame3.pack(side=BOTTOM)

success, img = capture.read()
height = img.shape[0]
width = img.shape[1]

label1 = Label(frame_1, width=int(width), height=int(height)-50)
label1.place(x=0, y=0)

name_var= StringVar()
passw_var= StringVar()

list = []
imageList = []



#label_widget = Label(app)   #Label to place frame data on 
#label_widget.pack()

offset = 20
imgSize = 300
counter = 0

#Declare label names
labels = ["A", "B", "C", "D", "E", "F", "G", "H",
          "I", "J", "K", "L", "M", "N", "O", "P",
          "Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z"]


def displayPhotos():
    for letter in list:
        match letter:
            case "A":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/A.jpg"))
                imageList.append(img)
                print ("Image found")
                labelA = Label(frame3, image = img).pack(side = LEFT)
            case "B":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/B.jpg"))
                imageList.append(img)
                print ("Image found")
                labelB = Label(frame3, image = img).pack(side = LEFT)
            case "C":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/C.jpg"))
                imageList.append(img)
                print ("Image found")
                labelC = Label(frame3, image = img).pack(side = LEFT)
            case "D":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/D.jpg"))
                imageList.append(img)
                print ("Image found")
                labelD = Label(frame3, image = img).pack(side = LEFT)
            case "E":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/E.jpg"))
                imageList.append(img)
                print ("Image found")
                labelE = Label(frame3, image = img).pack(side = LEFT)
            case "F":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/F.jpg"))
                imageList.append(img)
                print ("Image found")
                labelF = Label(frame3, image = img).pack(side = LEFT)
            case "G":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/G.jpg"))
                imageList.append(img)
                print ("Image found")
                labelG = Label(frame3, image = img).pack(side = LEFT)
            case "H":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/H.jpg"))
                imageList.append(img)
                print ("Image found")
                labelH = Label(frame3, image = img).pack(side = LEFT)
            case "I":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/I.jpg"))
                imageList.append(img)
                print ("Image found")
                labelI = Label(frame3, image = img).pack(side = LEFT)
            case "J":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/J.jpg"))
                imageList.append(img)
                print ("Image found")
                labelJ = Label(frame3, image = img).pack(side = LEFT)
            case "K":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/K.jpg"))
                imageList.append(img)
                print ("Image found")
                labelK = Label(frame3, image = img).pack(side = LEFT)
            case "L":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/L.jpg"))
                imageList.append(img)
                print ("Image found")
                labelL = Label(frame3, image = img).pack(side = LEFT)
            case "M":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/M.jpg"))
                imageList.append(img)
                print ("Image found")
                labelM = Label(frame3, image = img).pack(side = LEFT)
            case "N":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/N.jpg"))
                imageList.append(img)
                print ("Image found")
                labelN = Label(frame3, image = img).pack(side = LEFT)
            case "O":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/O.jpg"))
                imageList.append(img)
                print ("Image found")
                labelO = Label(frame3, image = img).pack(side = LEFT)
            case "P":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/P.jpg"))
                imageList.append(img)
                print ("Image found")
                labelP = Label(frame3, image = img).pack(side = LEFT)
            case "Q":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/Q.jpg"))
                imageList.append(img)
                print ("Image found")
                labelQ = Label(frame3, image = img).pack(side = LEFT)
            case "R":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/R.jpg"))
                imageList.append(img)
                print ("Image found")
                labelR = Label(frame3, image = img).pack(side = LEFT)
            case "S":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/S.jpg"))
                imageList.append(img)
                print ("Image found")
                labelS = Label(frame3, image = img).pack(side = LEFT)
            case "T":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/T.jpg"))
                imageList.append(img)
                print ("Image found")
                labelT = Label(frame3, image = img).pack(side = LEFT)
            case "U":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/U.jpg"))
                imageList.append(img)
                print ("Image found")
                labelU = Label(frame3, image = img).pack(side = LEFT)
            case "V":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/V.jpg"))
                imageList.append(img)
                print ("Image found")
                labelV = Label(frame3, image = img).pack(side = LEFT)
            case "W":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/W.jpg"))
                imageList.append(img)
                print ("Image found")
                labelW = Label(frame3, image = img).pack(side = LEFT)
            case "X":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/X.jpg"))
                imageList.append(img)
                print ("Image found")
                labelX = Label(frame3, image = img).pack(side = LEFT)
            case "Y":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/Y.jpg"))
                imageList.append(img)
                print ("Image found")
                labelY = Label(frame3, image = img).pack(side = LEFT)
            case "Z":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/Z.jpg"))
                imageList.append(img)
                print ("Image found")
                labelZ = Label(frame3, image = img).pack(side = LEFT)

def clearFrame():
    for widgets in frame3.winfo_children():
      widgets.destroy()

def submit():
    list.clear()   
    clearFrame()
 
    name=name_var.get()

    name = name.upper()
     
    name_var.set("")

    for x in name:
        list.append(x)

    for letter in list:
        print("Letter: " + letter)

    displayPhotos()

def handReader():
    global img
    success, img = capture.read()   #Capture frame data 

    global index
    imgOutput = img.copy()
    hands, img = detector.findHands(img,)    #find hands in img

    #if hand found, crop it out of frame
    if hands:
        hand = hands[0]
        x, y, width, height = hand['bbox']
        HandDataFromModel = np.ones((imgSize, imgSize, 3), np.uint8)*255
        imgCrop = img[y - offset:y + height + offset, x - offset:x + width + offset]
        imgCropShape = imgCrop.shape
        aspectRatio = height/width

        #Center cropped hand on white background - vertically 
        if (aspectRatio > 1):
            constant = imgSize/height
            calculatedWidth = math.ceil(constant*width)
            imgResize = cv2.resize(imgCrop, (calculatedWidth, imgSize))
            imgResizeShape = imgResize.shape
            widthGap = math.ceil((imgSize-calculatedWidth)/2)
            HandDataFromModel[:, widthGap:calculatedWidth + widthGap] = imgResize
            prediction, index = classifier.getPrediction(HandDataFromModel, draw=False)   #Get prediction of hand and index of label
            #print(prediction, index)    #Print prediction confidence and index of label to console

        #Center cropped hand on white background - horizontally 
        else:
            constant = imgSize/width
            calculatedHeight = math.ceil(constant*height)
            imgResize = cv2.resize(imgCrop, (imgSize, calculatedHeight))
            imgResizeShape = imgResize.shape
            HeightGap = math.ceil((imgSize-calculatedHeight)/2)
            HandDataFromModel[HeightGap:calculatedHeight + HeightGap, :] = imgResize

            prediction, index = classifier.getPrediction(HandDataFromModel, draw=False)   #Get prediction of hand and index of label
            #print(prediction, index)    #Print prediction confidence and index of label to console

        cv2.putText(imgOutput, labels[index], (x, y-40), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 2)
        cv2.rectangle(imgOutput, (x-offset, y-offset), (x+width+offset, y+height+offset), (255, 0, 255), 4)


    opencv_image = cv2.cvtColor(imgOutput, cv2.COLOR_BGR2RGBA)  #Convert colorspace from BGR->RGBA
    captured_image = Image.fromarray(opencv_image)  #Convert image from array format 

    photo_image = ImageTk.PhotoImage(image=captured_image)  #Convert frame data to image tkinter can use 


    label1.configure(image=photo_image)
    label1.image = photo_image

    # print(labels[index])

    win.after(10, handReader)


    # label_widget.photo_image = photo_image # Put frame on label 
    # label_widget.configure(image=photo_image) # configure image for label 

    # label_widget.after(10, handReader) # REPEAT

name_label = Label(frame2, text = 'Enter A Word', font=('calibre',10, 'bold')).pack(side=TOP)
# creating a entry for input
# name using widget Entry

name_entry = Entry(frame2,textvariable = name_var, font=('calibre',10,'normal')).pack(side=TOP)

sub_btn= Button(frame2,text = 'Show ASL Signs', command = submit).pack(side=TOP)


handReader()
win.mainloop()


