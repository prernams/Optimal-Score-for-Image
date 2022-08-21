from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pyrebase
import cv2
from sewar.full_ref import uqi
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import random
from PIL import Image, ImageTk


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

size_before = 0
size_after = 0

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


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def upload_file():
    f_types = [('Jpg Files', '*.jpg'),
               ('PNG Files', '*.png')]   # type of files to select
    filename = tk.filedialog.askopenfilename(filetypes=f_types)
    image_file = Image.open(filename)
    img = ImageTk.PhotoImage(image_file.resize((400, 400)))
    e1 = tk.Label(window)
    e1.place(
        x=49.0,
        y=186.0
    )
    e1.image = img
    label_before = tk.Label(
        text=('Original Image with size '+str(os.path.getsize(filename)/1000)+" KB."))
    label_before.place(
        x=150.0,
        y=600.0
    )
    e1['image'] = img
    score_reached = 0
    q = 10
    while(not score_reached):
        image_file.save("test_2.jpg", quality=q)
        img_1 = cv2.imread(filename)
        img_2 = cv2.imread("D:\\Prerana\\Techsurf\\test_2.jpg")
        print("Entered")
        score = uqi(img_1, img_2)
        if(score >= 0.95):
            score_reached = 1
        print(q, score)
        q += 2
    image_file.save("a.jpg", quality=q)
    img_after = Image.open("a.jpg")
    img_after = ImageTk.PhotoImage(img_after.resize((400, 400)))
    e2 = tk.Label(window)
    e2.place(
        x=600.0,
        y=186.0
    )
    e2.image = img_after
    e2['image'] = img_after
    label_after = tk.Label(text='Reduced Image with size ' +
                           str(os.path.getsize("a.jpg")/1000)+" KB.\n Optimal Score = "+str(q))
    label_after.place(
        x=700.0,
        y=600.0
    )
    # e2.image = img_after
    # e2['image'] = img_after
    # storage.child(filename.split('/')[-1]).put("a.jpg")
    # print(filename.split('/')[-1]+" Uploaded")


window = tk.Tk()

window.geometry("1000x1000")
window.title('Reducing Image Quality')
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=1000,
    width=1000,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
canvas.create_text(
    347.0,
    46.0,
    anchor="nw",
    text="Reducing Image Quality\n",
    fill="#000000",
    font=("JejuMyeongjo", 40 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: upload_file(),
    relief="flat"
)
button_1.place(
    x=456.0,
    y=97.0,
    width=242.0,
    height=64.0
)

window.resizable(True, True)
window.mainloop()
