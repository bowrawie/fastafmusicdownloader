import tkinter as tk
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
from urllib.request import urlopen
from bs4 import BeautifulSoup as sp
from mdv2 import DOWNLOADER as down
import time
from functools import partial

def GetImage(img_url,rawurl):
    root = tk.Tk()
    root.title("FASTAF Music Downloader")
    root.iconbitmap('ytb.ico')
    response = requests.get(img_url)
    img_data = response.content
    image1 = Image.open(BytesIO(img_data))
    image2 = image1.resize((400, 230), Image.ANTIALIAS)
    image3 = ImageTk.PhotoImage(image2)
    canvas = tk.Canvas(root)
    canvas.pack()
    soup = sp(urlopen(rawurl), "lxml")
    Title = soup.title.string
    STitle = Title.replace("- YouTube","")
    text1 = "Downloaded "+STitle+" !"
    canvas.create_text(180,250,fill="darkblue",font="Times 10 ",text=text1)
    canvas.create_image(0, 0, anchor=tk.NW, image=image3)
    canvas.update
    BtnSubmit=tk.Button(root, text="Submit" ,
                  command=partial(down(rawurl))
                  ).grid(row=3,column=3)
    BtnSubmit.pack()
    root.mainloop()
    

    



