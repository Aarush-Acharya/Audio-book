from tkinter import *

import PyPDF2 as reader
from gtts import gTTS
from playsound import playsound

pratham = Tk()

pratham.geometry("500x500")

pratham.title("PDFA")


def hello():
    filename = fileentry.get()
    with open(filename, "rb") as file:
        pdf = reader.PdfFileReader(file)
        print(pdf.numPages)
        page = pdf.getPage(0)
        text = page.extractText()
        print(text)
        tts = gTTS(text)
        tts.save("0.mp3")
        playsound("0.mp3")


label1 = Label(pratham, text="Enter the file name")
label1.pack()
filen = StringVar()
fileentry = Entry(pratham, textvariable=filen)
fileentry.pack()

b1 = Button(pratham, text="Submit", command=hello)
b1.pack()
b2 = Button(pratham, text="Start/Stop")
b2.pack()
pratham.mainloop()
