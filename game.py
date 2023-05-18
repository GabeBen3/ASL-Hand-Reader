import cv2
import numpy as np
import pygame
import math
import time
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier

from pygame.locals import(K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)

detector = HandDetector(maxHands=1) #Detect Hands in capture, 1 hand
classifier = Classifier("Model/keras_model.h5", "Model/labels.txt") #Call Model for classification

offset = 20
imgSize = 300
counter = 0

labels = ["A", "B", "C", "D", "E", "F", "G", "H",
          "I", "J", "K", "L", "M", "N", "O", "P",
          "Q", "R","S", "T", "U", "V", "W", "X", "Y", "Z"]

capture = cv2.VideoCapture(0)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption('ASL Helper')

# img = cv2.imread("SignPhotos/A.jpg")

surf = pygame.Surface((500, 500))

# pygame.surfarray.blit_array(surf, img.swapaxes(0, 1))



# imp = pygame.image.load(img).convert()

# screen.blit(surf, (0, 0))

pygame.display.flip()

running = True

while running: 


    

    ret, img = capture.read()


    height = int(img.shape[0]*0.9)
    width = int(img.shape[1]*0.9)
    img = cv2.resize(img, (width, height))
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = np.rot90(img)
    img = pygame.surfarray.make_surface(img)
    screen.blit(img, (0,0))
    pygame.display.update()



    for event in pygame.event.get():

        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False





