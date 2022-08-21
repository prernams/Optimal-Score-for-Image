# -------------------------------------------------------------------------------
# Imports
import pyrebase
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk

# -------------------------------------------------------------------------------
# Variables & Setup

filelist = [f for f in os.listdir(".") if f.endswith(".JPG")]
for f in filelist:
    os.remove(os.path.join(".", f))

firebaseConfig = {
    "apiKey": "AIzaSyCu1U55lhQfbDnYnCxyneSzFRANF5-4TxU",
    "authDomain": "upload-file-fa45d.firebaseapp.com",
    "projectId": "upload-file-fa45d",
    "storageBucket": "upload-file-fa45d.appspot.com",
    "messagingSenderId": "530952354447",
    "appId": "1:530952354447:web:b29bc33c32b09492980efa",
    "measurementId": "G-B145PYMNVH",
    "databaseURL": ""
}

firebase_storage = pyrebase.initialize_app(firebaseConfig)
storage = firebase_storage.storage()

my_w = tk.Tk()
my_w.geometry("410x300")  # Size of the window
my_w.title('Reducing Image Quality')
my_font1 = ('times', 18, 'bold')
l1 = tk.Label(my_w, text='Reducing Image Quality', width=30, font=my_font1)
l1.grid(row=1, column=1, columnspan=4)
b1 = tk.Button(my_w, text='Upload Image',
               width=20, command=lambda: upload_file())
b1.grid(row=2, column=1, columnspan=4)


def upload_file():
    f_types = [('Jpg Files', '*.jpg'),
               ('PNG Files', '*.png')]   # type of files to select
    filename = tk.filedialog.askopenfilename(filetypes=f_types)
    image_file = Image.open(filename)
    img = ImageTk.PhotoImage(image_file.resize((500, 500)))
    e1 = tk.Label(my_w)
    e1.grid(row=5, column=1)
    e1.image = img
    label_before = tk.Label(
        text=('Original Image with size '+str(os.path.getsize(filename)/1000)+" KB"))
    label_before.grid(column=1, row=6)
    e1['image'] = img
    image_file.save("a.jpg", quality=6)
    img_after = Image.open("a.jpg")
    img_after = ImageTk.PhotoImage(img_after.resize((500, 500)))
    e2 = tk.Label(my_w)
    e2.grid(row=5, column=15)
    label_after = tk.Label(
        text='Reduced Image with size ' + str(os.path.getsize("a.jpg")/1000)+" KB")
    label_after.grid(column=15, row=6)
    e2.image = img_after
    e2['image'] = img_after
    storage.child(filename.split('/')[-1]).put("a.jpg")
    print("File Uploaded")


my_w.mainloop()  # Keep the window open
