from ast import operator
import numbers
from argparse import MetavarTypeHelpFormatter
from distutils import command
from tkinter import*
from tokenize import Number
from unittest.util import strclass
#import math
from math import*


mansLogs=Tk()
mansLogs.title('Kalkulators')
#mansLogs.geometry('300x300')
#poga=Button(mansLogs,text='Labdien!',bg='purple',fg='pink')
#poga.pack()

e=Entry(mansLogs,width=15,bd=30,bg="gray",font=("Arial Black",20))
e.grid(row=0,column=0,columnspan=4)

btnclear=Button(mansLogs,text='C',padx='40',pady='20',bd=10,bg="orange", command=lambda:clear())
btnclear.grid(row=1,column=0)

btn0=Button(mansLogs,text='0',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnClick(0))
btn1=Button(mansLogs,text='1',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnClick(1))
btn2=Button(mansLogs,text='2',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnClick(2))
btn3=Button(mansLogs,text='3',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnClick(3))
btn4=Button(mansLogs,text='4',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnClick(4))
btn5=Button(mansLogs,text='5',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnClick(5))
btn6=Button(mansLogs,text='6',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnClick(6))
btn7=Button(mansLogs,text='7',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnClick(7))
btn8=Button(mansLogs,text='8',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnClick(8))
btn9=Button(mansLogs,text='9',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnClick(9))
btnminus=Button(mansLogs,text='-',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnCommand("-"))
btnplus=Button(mansLogs,text='+',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnCommand("+"))
btndivide=Button(mansLogs,text='/',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnCommand("/"))
btnmultiply=Button(mansLogs,text='*',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnCommand("*"))
btnequal=Button(mansLogs,text='=',padx='90',pady='20',bd=10,bg="orange",command=lambda:Equals())
btnsqr=Button(mansLogs,text='sqrt',padx='30',pady='20',bd=10,bg="orange",command=lambda:sqrt())
btnpow=Button(mansLogs,text='^',padx='40',pady='20',bd=10,bg="orange",command=lambda:btnCommand("^"))
btnlog=Button(mansLogs,text='log(10)',padx='25',pady='20',bd=10,bg="orange",command=lambda:logg())



btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
btndivide.grid(row=2,column=3)

btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
btnmultiply.grid(row=5,column=1)

btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)
btnminus.grid(row=3,column=3)

btn0.grid(row=5,column=0)
btnequal.grid(row=5,column=2,columnspan=2)
btnplus.grid(row=4,column=3)

btnsqr.grid(row=1,column=1)
btnpow.grid(row=1,column=2)
btnlog.grid(row=1,column=3)


def sqrt():
  num1=int(e.get())
  result=0
  result=num1**0.5
  e.delete(0,END)
  e.insert(0,str(result))
  return 0

def logg():
  num1=int(e.get())
  result=0
  result=log10(num1)
  e.delete(0,END)
  e.insert(0,str(result))
  return 0


def btnClick(number):
  current=e.get() #nolasa eso??o skaitli
  e.delete(0,END) #nodzes
  newNumber=str(current)+str(number) 
  e.insert(0,newNumber) #ievieto displeja
  return 0

def btnCommand(command):
    global number
    global num1
    global mathOp 
    mathOp=command
    num1=int(e.get())
    e.delete(0,END)
    return 0


def Equals():
    num2=int(e.get())
    result=0
    if mathOp=="+":
        result=num1+num2
    elif mathOp=="-":
        result=num1-num2
    elif mathOp=="/":
        result=num1/num2
    elif mathOp=="*":
        result=num1*num2
    elif mathOp=="^":
        result=num1**num2
    
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def clear():
     e.delete(0,END)




# command=lambda:btnClick(0) #funkcijai padod parametrus


mansLogs.mainloop()