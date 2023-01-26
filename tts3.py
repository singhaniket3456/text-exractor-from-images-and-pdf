from distutils.command.upload import upload
import tkinter as tk
from token import LEFTSHIFT
from playsound import playsound
from gtts import gTTS
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os
from PIL import Image, ImageTk
import pytesseract
from PIL import Image
import PyPDF2 as pdf
from distutils.filelist import translate_pattern
from googletrans import Translator
import json

with open('languages.json') as json_file:
	data = json.load(json_file)
Key = data.keys()
List_key = list(Key)
Value = data.values()
List_val = list(Value)

# Combo_box_data=dict(zip(List_key, List_val))

root = Tk()
root.title("TRANSLATOR")
root.geometry("900x600+200+200")
root.resizable(False, False)
root.configure(bg="#00e0ff")

engine = pyttsx3.init()


def speaknow():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
            setvoice()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            setvoice()
            engine.runAndWait()
        else:
            engine.setProperty('rate', 60)
            setvoice()
            engine.runAndWait()

def speaknow2():
    text = text_area1.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
            setvoice()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            setvoice()
            engine.runAndWait()
        else:
            engine.setProperty('rate', 60)
            setvoice()
            engine.runAndWait()


import time

def speaknow3():
        
        t = time.time()
        ml = int(t * 1000)
        langcombo = lang_combobox.get()
        text = text_area1.get(1.0, END)
        print(text)
        filename = "tts"+langcombo+str(ml)+".mp3"
        tts = gTTS(text,lang=langcombo)
        tts.save(filename)
        playsound(filename)


def download():
    text = text_area.get(1.0, END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    def setvoice():
        if gender == 'Male':
            engine.setProperty('voice', voices[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text, 'text.mp3')
            engine.runAndWait()

    if text:
        if speed == "Fast":
            engine.setProperty('rate', 250)
            setvoice()
        elif speed == 'Normal':
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate', 60)
            setvoice()


def upload():
    f_types = [('png', '.png'), ('jpg', '.jpg'), ('pdf', '*.pdf')]
    x = (".png", ".jpg")
    y = (".pdf")
    filepath = filedialog.askopenfilename(multiple=False, filetypes=f_types)
    if filepath.endswith(x):
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
        image = Image.open(filepath)
        image_to_text = pytesseract.image_to_string(image, lang='eng')
        print(image_to_text)
        text_area.insert('end', image_to_text)

    elif filepath.endswith(y):
        a = pdf.PdfFileReader(filepath)
        number_of_pages = len(a.pages)
        print(number_of_pages)
        num = 0
        for num in range(number_of_pages):
            page = a.pages[num]
            text = page.extract_text()
            print(text)
            text_area.insert('end', text)

    else:
        print("Unsupported File Type")


translater = Translator()


def trans():
    langcombo = lang_combobox.get()
    text = text_area.get(1.0, END)
    detect = translater.detect(text)
    d = detect.lang
    print(d)

    i = 0
    for i in range(len(List_key)):
        if langcombo == List_key[i]:
            out = translater.translate(text, dest=List_key[i])
            trtext = out.text
            text_area1.insert('end', trtext+"\n")
        else : pass

def translatedVoice():
    langcombo = lang_combobox.get()
    text = text_area1.get(1.0, END)
    print(text)
    if langcombo in {'hi','ja','ru','zh-tw','zh-cn','ko','te','th','ta','mr','th','vi','ur'}:
        speaknow3()
    else:speaknow2()
        

bg = PhotoImage(file = "images/BG1.png")


canvas1 = Canvas( root, width = 900,
                 height = 600)

canvas1.pack(fill = "both", expand = True)

canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")

image_icon = PhotoImage(file="images/translater.png")
root.iconphoto(False, image_icon)

# Top Frame
Top_frame = Frame(root, bg="white", width=1100, height=70)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="images/translater.png")
Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)
Label(Top_frame, text="TRANSLATOR", font="Gigi 20 bold",
      bg="white", fg="black").place(x=80, y=15)

######
scrol_bar = Scrollbar(root, orient=VERTICAL)
scrol_bar.pack(side=RIGHT, fill=Y)
text_area = Text(root, font="robote 20", bg="white",
                 relief=GROOVE, wrap=WORD, yscrollcommand=scrol_bar.set)
text_area.place(x=10, y=150, width=450, height=150)

scrol_bar.config(command=text_area.yview)

text_area1 = Text(root, font="robote 20", bg="white",
                  relief=GROOVE, wrap=WORD, yscrollcommand=scrol_bar.set)
text_area1.place(x=10, y=400, width=450, height=150)

scrol_bar.config(command=text_area1.yview)

Label(root, text="VOICE", font="Gigi 15 bold",
      bg="#305065", fg="white").place(x=580, y=160)
Label(root, text="SPEED", font="Gigi 15 bold",
      bg="#305065", fg="white").place(x=760, y=160)

# combo box
gender_combobox = Combobox(
    root, values=['Male', 'Female'], font="Gigi 14", state='r', width=10)
gender_combobox.place(x=550, y=200)
gender_combobox.set('Male')

# speed combobox
speed_combobox = Combobox(
    root, values=['Fast', 'Normal', 'Slow'], font="Gigi 14", state='r', width=10)
speed_combobox.place(x=730, y=200)
speed_combobox.set('Normal')

# translate combobox
imageicon4 = PhotoImage(file="images/translate.png")

tr = Button(root, text="Translate", compound=LEFT, image=imageicon4, width=200, bg="#39c790", font="Gigi 14 bold",
            command=trans)
tr.place(x=10, y=335)

lang_combobox = Combobox(
    root, values=(List_key), font="Gigi 14", state='r', width=5)
lang_combobox.place(x=230, y=345)
lang_combobox.set('fr')

imageicon = PhotoImage(file="images/speak.png")
btn = Button(root, text="Speak", compound=LEFT, image=imageicon,
             width=130,bg="#39c790" ,font="Gigi 14 bold", command=speaknow)
btn.place(x=550, y=280)

imageicon2 = PhotoImage(file="images/download.png")
save = Button(root, text="Save", compound=LEFT, image=imageicon2, width=130, bg="#39c790", font="Gigi 14 bold",
              command=download)
save.place(x=730, y=280)

imageicon3 = PhotoImage(file="images/Upload 1.png")
save = Button(root, text="Upload", compound=LEFT, image=imageicon3, width=200, bg="#39c790", font="Gigi 14 bold",
              command=upload)
save.place(x=10, y=82)

imageicon5 = PhotoImage(file="images/speak.png")
save = Button(root, text="Speak", compound=LEFT, image=imageicon5, width=130, bg="#39c790", font="Gigi 14 bold",
              command=translatedVoice)
save.place(x=550, y=454)


root.mainloop()
