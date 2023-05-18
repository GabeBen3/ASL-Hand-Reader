from tkinter import * 
from PIL import ImageTk, Image

win=Tk()
 
# setting the windows size
win.geometry("600x400")
frame1 = Frame(win, width=600, height=400, bg="skyblue").place(x=0, y=0)
frame2 = Frame(win, width=600, height=125, bg = "skyblue")
frame2.pack(side=BOTTOM)

# declaring string variable
# for storing name and password
name_var= StringVar()
passw_var= StringVar()

list = []
imageList = []
 
  
# defining a function that will
# get the name and password and
# print them on the screen

def clearFrame():
    for widgets in frame2.winfo_children():
      widgets.destroy()

def displayPhotos():
    for letter in list:
        match letter:
            case "A":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/A.jpg"))
                imageList.append(img)
                print ("Image found")
                labelA = Label(frame2, image = img).pack(side = LEFT)
            case "B":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/B.jpg"))
                imageList.append(img)
                print ("Image found")
                labelB = Label(frame2, image = img).pack(side = LEFT)
            case "C":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/C.jpg"))
                imageList.append(img)
                print ("Image found")
                labelC = Label(frame2, image = img).pack(side = LEFT)
            case "D":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/D.jpg"))
                imageList.append(img)
                print ("Image found")
                labelD = Label(frame2, image = img).pack(side = LEFT)
            case "E":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/E.jpg"))
                imageList.append(img)
                print ("Image found")
                labelE = Label(frame2, image = img).pack(side = LEFT)
            case "F":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/F.jpg"))
                imageList.append(img)
                print ("Image found")
                labelF = Label(frame2, image = img).pack(side = LEFT)
            case "G":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/G.jpg"))
                imageList.append(img)
                print ("Image found")
                labelG = Label(frame2, image = img).pack(side = LEFT)
            case "H":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/H.jpg"))
                imageList.append(img)
                print ("Image found")
                labelH = Label(frame2, image = img).pack(side = LEFT)
            case "I":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/I.jpg"))
                imageList.append(img)
                print ("Image found")
                labelI = Label(frame2, image = img).pack(side = LEFT)
            case "J":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/J.jpg"))
                imageList.append(img)
                print ("Image found")
                labelJ = Label(frame2, image = img).pack(side = LEFT)
            case "K":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/K.jpg"))
                imageList.append(img)
                print ("Image found")
                labelK = Label(frame2, image = img).pack(side = LEFT)
            case "L":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/L.jpg"))
                imageList.append(img)
                print ("Image found")
                labelL = Label(frame2, image = img).pack(side = LEFT)
            case "M":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/M.jpg"))
                imageList.append(img)
                print ("Image found")
                labelM = Label(frame2, image = img).pack(side = LEFT)
            case "N":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/N.jpg"))
                imageList.append(img)
                print ("Image found")
                labelN = Label(frame2, image = img).pack(side = LEFT)
            case "O":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/O.jpg"))
                imageList.append(img)
                print ("Image found")
                labelO = Label(frame2, image = img).pack(side = LEFT)
            case "P":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/P.jpg"))
                imageList.append(img)
                print ("Image found")
                labelP = Label(frame2, image = img).pack(side = LEFT)
            case "Q":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/Q.jpg"))
                imageList.append(img)
                print ("Image found")
                labelQ = Label(frame2, image = img).pack(side = LEFT)
            case "R":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/R.jpg"))
                imageList.append(img)
                print ("Image found")
                labelR = Label(frame2, image = img).pack(side = LEFT)
            case "S":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/S.jpg"))
                imageList.append(img)
                print ("Image found")
                labelS = Label(frame2, image = img).pack(side = LEFT)
            case "T":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/T.jpg"))
                imageList.append(img)
                print ("Image found")
                labelT = Label(frame2, image = img).pack(side = LEFT)
            case "U":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/U.jpg"))
                imageList.append(img)
                print ("Image found")
                labelU = Label(frame2, image = img).pack(side = LEFT)
            case "V":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/V.jpg"))
                imageList.append(img)
                print ("Image found")
                labelV = Label(frame2, image = img).pack(side = LEFT)
            case "W":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/W.jpg"))
                imageList.append(img)
                print ("Image found")
                labelW = Label(frame2, image = img).pack(side = LEFT)
            case "X":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/X.jpg"))
                imageList.append(img)
                print ("Image found")
                labelX = Label(frame2, image = img).pack(side = LEFT)
            case "Y":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/Y.jpg"))
                imageList.append(img)
                print ("Image found")
                labelY = Label(frame2, image = img).pack(side = LEFT)
            case "Z":
                img = ImageTk.PhotoImage(Image.open("SignPhotos/Z.jpg"))
                imageList.append(img)
                print ("Image found")
                labelZ = Label(frame2, image = img).pack(side = LEFT)
                  
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



name_label = Label(frame1, text = 'Username', font=('calibre',10, 'bold'))
# creating a entry for input
# name using widget Entry
name_entry = Entry(frame1,textvariable = name_var, font=('calibre',10,'normal'))


  
# creating a label for password
  
# creating a button using the widget
# Button that will call the submit function
sub_btn= Button(frame1,text = 'Submit', command = submit)
  
# placing the label and entry in
# the required position using grid
# method

# for letter in imageList:
#     label = str(letter)
#     globals()[label] = Label(win, image = imageList[letter])
#     label.pack()

name_label.place(x=0, y=0)
name_entry.place(x =0, y= 50)
sub_btn.place(x=0, y= 100)

win.mainloop()