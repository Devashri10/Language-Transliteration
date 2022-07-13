#Libraries
from lib2to3.pytree import convert
from turtle import bgcolor
from googletrans import Translator ,LANGUAGES
from gtts import gTTS
from tkinter import *
from tkinter import ttk

#creating a window
window =Tk()
window.title("Language Transliteration")
window.geometry('800x500')
window.configure(bg='lightgray')
set_bg =PhotoImage(file ="C:\python\Language translitration\image for background.png")
label = Label(window,image=set_bg)
label.place( x=0,y= -100)

#adding text Box input output
Label(window,text ="Enter Text", font = 'arial 13 bold', bg ='white smoke').place(x=260,y=130)
entry = Entry(window, bg ="darkgray",fg="black",font =("Aparajita",25,"bold"))
entry.place(x=260,y=150)
Label(window,text ="Output", font = 'arial 13 bold', bg ='white smoke').place(x=175,y=230)
output= Text(window,bg="darkgray",fg="black",height = 2,padx=5, pady= 5, width =32,font =("Aparajita",25,"bold"))
output.place(x=180,y=250)

#comboBox
language = list(LANGUAGES.values())

src_lang = ttk.Combobox(window, values= language, width =22)
src_lang.place(x=100,y=150)
src_lang.set('choose input language')

dest_lang = ttk.Combobox(window, values = language, width =22)
dest_lang.place(x=20,y=250)
dest_lang.set('choose output language')

#Translator
def Translate():
    translator = Translator()
    translated=translator.translate(text= entry.get() , src = src_lang.get(), dest = dest_lang.get())
    output.delete(1.0, END)
    output.insert(END, translated.text)

#Translator Button
trans_btn = Button(window, text = 'Translate',font = 'arial 12 bold',pady = 5,command = Translate , bg = 'royal blue1', activebackground = 'sky blue')

trans_btn.place(x = 350, y= 350 )


window.mainloop()
