from tkinter import *
import pyttsx3
from tkinter import filedialog
import os
from tkinter.ttk import Combobox


root=Tk()
root.title("Text to speech")
root.geometry("900x450")
root.resizable(False,False)
root.config(bg="lightgray")

icon = "favicon.ico"
root.wm_iconbitmap(icon)

main=pyttsx3.init()

def Speak():
    user=text_area.get(1.0,END)
    gender=voice_gender.get()
    speed=voice_speed.get()
    voice=main.getProperty('voices')

    def setvoice():
        if (gender=="Male"):
            main.setProperty("voice",voice[0].id)
            main.say(user)
            main.runAndWait()
        else:
            main.setProperty("voice",voice[1].id)
            main.say(user)
            main.runAndWait()

    if(user):
        if(speed=="Fast"):
            main.setProperty("rate",250)
            setvoice()
        if(speed=="Normal"):
            main.setProperty("rate",150)
            setvoice()
        else:
            main.setProperty("rate",60)
            setvoice()


def Save():
    user=text_area.get(1.0,END)
    gender=voice_gender.get()
    speed=voice_speed.get()
    voice=main.getProperty('voices')

    def setvoice():
        if (gender=="Male"):
            main.setProperty("voice",voice[0].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            main.save_to_file(user,"text.mp3")
            main.runAndWait()
        else:
            main.setProperty("voice",voice[1].id)
            path = filedialog.askdirectory()
            os.chdir(path)
            main.save_to_file(user,"text.mp3")
            main.runAndWait()

    if(user):
        if(speed=="Fast"):
            main.setProperty("rate",250)
            setvoice()
        if(speed=="Normal"):
            main.setProperty("rate",150)
            setvoice()
        else:
            main.setProperty("rate",60)
            setvoice()




Label(root,text="Text To Voice",fg=("#2C2D2D"),bg="lightgrey",font="arieal 24").pack(anchor="center",pady=50)

text_area = Text(root,font="arieal 18",bg="white",relief="groove",wrap=WORD)
text_area.insert("1.0", "Enter text to speak")
text_area.place(x=10,y=150,width=500,height=250)

Label(root,text="Select Voice:-",fg=("#2C2D2D"),bg="lightgrey",font=18).place(relx=0.6,rely=0.33)

Label(root,text="Speed of Voice:-",fg=("#2C2D2D"),bg="lightgrey",font=18 ).place(relx=0.8,rely=0.33)

voice_gender = Combobox(root,values=["Male","Female"],state="r",width=15,font="arieal 10")
voice_gender.place(relx=0.61,rely=0.42)
voice_gender.set("Male")
voice_speed = Combobox(root,values=["Slow","Normal","Fast"],state="r",width=15,font="arieal 10")
voice_speed.place(relx=0.81,rely=0.42)
voice_speed.set("normal")

start=Button(root,text="Speak",bg="white",fg="black",width=10,font=18,command=Speak).place(relx=0.6,rely=0.58)

save = Button(root,text="Save",bg="white",fg="black",width=10,font=18,command=Save).place(relx=0.8,rely=0.58)


root.mainloop()

