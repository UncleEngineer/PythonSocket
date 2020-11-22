# GUI-Chat.py
from tkinter import *
from tkinter import ttk
import tkinter.scrolledtext as st

GUI = Tk()
GUI.geometry('650x750+1000+100')
GUI.title('โปรแกรมแชทไปหาลุง')

FONT1 = ('Angsana New',35) 
FONT2 = ('Angsana New',20) 
#############chatbox###############
F1 = Frame(GUI)
F1.place(x=5,y=5)

allmsg = StringVar()

chatbox = st.ScrolledText(F1,width=38,heigh=10,font=FONT1)
chatbox.pack(expand=True, fill='x')
#############message form###############
v_msg = StringVar()

F2 = Frame(GUI)
F2.place(x=20,y=650)

E1 = ttk.Entry(F2,textvariable=v_msg,font=FONT2,width=50)
E1.pack(ipady=20)

#############button###############
def SendMessage(event=None):
	msg = v_msg.get()
	allmsg.set(allmsg.get() + msg + '\n---\n')
	chatbox.delete(1.0,END) # clear old msg
	chatbox.insert(INSERT,allmsg.get()) # insert new
	chatbox.yview(END)
	v_msg.set('') # clear msg
	E1.focus()

F3 = Frame(GUI)
F3.place(x=500,y=650)
B1 = ttk.Button(F3,text='Send',command=SendMessage)
B1.pack(ipadx=25,ipady=30)

E1.bind('<Return>',SendMessage)

GUI.mainloop()