#Code by Jake Feeney. This only counts down to midnight so only put it on at new years eve.
from Tkinter import *
import time, math
window = Tk()
window.title("New Year Countdown")
display = Entry(window,font=("Calibri",100), bg="light green")
display.grid(row=0, column=0, columnspan=2, sticky=N)
text=Label(window, text="Code by Jake Feeney.\nwww.lptcdojo.com")
text.grid(row=1,column=0,sticky=W)
def setcurrenttime(time):
    display.delete(0, END)
    display.insert(END, time)
def giveseconds():
    #These are how many seconds in a hour, a minute + a day
    hour = 3600
    minute = 60
    hsec= int(time.strftime("%H")) * hour
    msec= int(time.strftime("%M")) * minute
    bsec= int(time.strftime("%S"))
    sec = bsec + msec + hsec
    return sec
def caluclatetime():
    day = 86400
    totalsec = giveseconds()
    print totalsec
    time = day - totalsec
    sec = time % 60
    minutes = int(math.ceil(time/60))
    hour = int(math.ceil(minutes/60))
    minutes = minutes % 60
    countdown = str(hour) + ":" + str(minutes) + ":" + str(sec)
    
    if totalsec < 30:
        setcurrenttime("Happy New Year!!!")
    else:
        setcurrenttime(countdown)
    window.after(1000, caluclatetime)

window.after(1000, caluclatetime)
window.mainloop()
