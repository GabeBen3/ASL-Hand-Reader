# USE <pip install -r requirements.txt> IN COMMAND LINE TO INSTALL ALL REQUIRED PACKAGES
#
# Use this file to capture position of finger markers from opencv hand detector
# Images of position  markers will be used to train AI model 
# Train new version of tensorflow model by adding photos captured in this file
    # Launch to start hand sign capture
    # Make Sign in ASL 
    # Hold q to continuously take series of photos - save photos to corresponding file in /HandData
    # Move hand around in various positions/basic rotations for more accurate model
    #
    # Upload /HandaData images to https://teachablemachine.withgoogle.com/train to train new model, use CAPS when naming a class
    # Export model as Tensorflow-Keras-Keras
    # Replace files in in /Model
# Bugs: 
    # Left/Right hand display is flipped
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

capture = cv2.VideoCapture(0)   #Start capture
detector = HandDetector(maxHands=1) #launch hand detector for 1 hand
offset = 20     #offset and resolution of background to display hand sign onto 
imgSize = 300
imgCounter = 0     #Number of photos taken 

folder = "HandData/Z"   

while True: 
    success, img = capture.read()       #Capture Frame data
    hands, img = detector.findHands(img)    #Capture Hand Detector Data 

    imageBeingSaved = np.ones((imgSize, imgSize, 3), np.uint8)*255
    imageBeingSaved = cv2.flip(imageBeingSaved, 1)

    if hands:
        hand = hands[0]     #identify hand

        x, y, width, height = hand['bbox']      #pull data from detector

        imgCrop = img[y - offset:y + height + offset, x - offset:x + width + offset]    

        imgCropShape = imgCrop.shape

        aspectRatio = height/width

        # Resize images being captured
        if (aspectRatio > 1): 
            constant = imgSize/height

            calculatedWidth = math.ceil(constant*width)

            imgResize = cv2.resize(imgCrop, (calculatedWidth, imgSize))

            imgResizeShape = imgResize.shape

            widthGap = math.ceil((imgSize-calculatedWidth)/2)

            imageBeingSaved[:, widthGap:calculatedWidth + widthGap] = imgResize

        else:
            constant = imgSize/width

            calculatedHeight = math.ceil(constant*height)

            imgResize = cv2.resize(imgCrop, (imgSize, calculatedHeight))

            imgResizeShape = imgResize.shape

            HeightGap = math.ceil((imgSize-calculatedHeight)/2)

            imageBeingSaved[HeightGap:calculatedHeight + HeightGap, :] = imgResize

        cv2.flip(imageBeingSaved, 1)
    
    #Display Capture and Image being saved
    cv2.imshow("Image Being Saved", cv2.flip(imageBeingSaved, 1))
    cv2.imshow("Capture", cv2.flip(img, 1))
    key = cv2.waitKey(1)


    if key == ord("q"):     
        cv2.imwrite(f'{folder}/Image_{time.time()}.jpg',imageBeingSaved)
        imgCounter += 1
        print (imgCounter)
