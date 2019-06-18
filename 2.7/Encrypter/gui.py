import encrypter as enc
from Tkinter import *

def encrypt():
    outputbox.delete(0.0, END)
    outputbox.insert(END, enc.encrypt(passbox.get(), msgbox.get("1.0", END)))
def randompassword():
    passbox.delete(0, END)
    passbox.insert(END,enc.generatepassword("abcdefghijklmnopqrstuvwxyz .!;,?"))
window=Tk()
window.title("Encrypter")

txt1=Label(window, text="Enter your message here:")
msgbox=Text(window, bg="white", height=20, width=60)
enter=Button(window, text="Encode/Decode", width=15, command=encrypt)
txt2=Label(window, text="Enter your password here:")
passbox=Entry(window, width=80, bg="white")
randpass=Button(window, text="Generate a random password", width=25, command=randompassword)
txt3=Label(window, text="Encoded/Decoded message:")
outputbox=Text(window, bg="white", height=20, width=60)


msgbox.delete(0.0, END)
msgbox.insert(END,"The quick brown fox jumps over the lazy dog.")

txt1.grid(row=0,column=0, sticky=W)
msgbox.grid(row=1,column=0, sticky=W)
enter.grid(row=1,column=1, sticky=SW)
txt2.grid(row=2,column=0, sticky=W)
passbox.grid(row=3,column=0, sticky=W)
randpass.grid(row=3,column=1, sticky=W)
txt3.grid(row=4,column=0, sticky=W)
outputbox.grid(row=5, column=0, sticky=W)

window.mainloop()
