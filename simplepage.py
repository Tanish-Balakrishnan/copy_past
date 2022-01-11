import pyautogui
import time
from tkinter import *
from tkinter import scrolledtext
from tkinter import ttk

import tkinter as tk
def pyauto():
    time.sleep(5)
    pyautogui.write(text_area.get("1.0",END))
    
window=Tk()
btn=Button(window, text="   Run   ", fg='red',bg='green',font=("Helvetica", 20),command = pyauto)
btn.place(x=250, y=120)
lbl=Label(window, text="you can paste in the text field", bg='red', font=("Helvetica", 16))
lbl.place(x=150, y=50)
text_area = scrolledtext.ScrolledText(wrap=tk.WORD,width=40, height=8)
  
text_area.place(x=100, y=190,width=600,height=500)
window.title('Simplepage
window.configure(bg='#347DA6')
window.geometry("800x800+100+100")

text_area.focus()
window.mainloop()
