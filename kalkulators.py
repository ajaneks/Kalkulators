from argparse import MetavarTypeHelpFormatter
from distutils import command
from tkinter import*
from tokenize import Number
mansLogs=Tk()
mansLogs.title('Kalkulators')
#mansLogs.geometry('300x300')
#poga=Button(mansLogs,text='Labdien!',bg='purple',fg='pink')
#poga.pack()

e=Entry(mansLogs,width=15,font=("Arial Black",20))
e.grid(row=0,column=0,columnspan=4)

btnclear=Button(mansLogs,text='C',padx='120',pady='20', command=lambda:clear())
btnclear.grid(row=1,column=0,columnspan=3)

btn0=Button(mansLogs,text='0',padx='80',pady='20',command=lambda:btnClick(0))
btn1=Button(mansLogs,text='1',padx='40',pady='20',command=lambda:btnClick(1))
btn2=Button(mansLogs,text='2',padx='40',pady='20',command=lambda:btnClick(2))
btn3=Button(mansLogs,text='3',padx='40',pady='20',command=lambda:btnClick(3))
btn4=Button(mansLogs,text='4',padx='40',pady='20',command=lambda:btnClick(4))
btn5=Button(mansLogs,text='5',padx='40',pady='20',command=lambda:btnClick(5))
btn6=Button(mansLogs,text='6',padx='40',pady='20',command=lambda:btnClick(6))
btn7=Button(mansLogs,text='7',padx='40',pady='20',command=lambda:btnClick(7))
btn8=Button(mansLogs,text='8',padx='40',pady='20',command=lambda:btnClick(8))
btn9=Button(mansLogs,text='9',padx='40',pady='20',command=lambda:btnClick(9))
btnminus=Button(mansLogs,text='-',padx='40',pady='20',command=lambda:btnCommand("-"))
btnplus=Button(mansLogs,text='+',padx='40',pady='20',command=lambda:btnCommand("+"))
btndivide=Button(mansLogs,text='/',padx='40',pady='20',command=lambda:btnCommand("/"))
btnmultiply=Button(mansLogs,text='x',padx='40',pady='20',command=lambda:btnCommand("*"))
btnpoint=Button(mansLogs,text='.',padx='40',pady='20')
btnequal=Button(mansLogs,text='=',padx='40',pady='20',command=lambda:Equals())


btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)
btndivide.grid(row=1,column=3)

btn4.grid(row=3,column=0)
btn5.grid(row=3,column=1)
btn6.grid(row=3,column=2)
btnmultiply.grid(row=2,column=3)

btn1.grid(row=4,column=0)
btn2.grid(row=4,column=1)
btn3.grid(row=4,column=2)
btnminus.grid(row=3,column=3)

btnpoint.grid(row=5,column=2)
btn0.grid(row=5,column=0,columnspan=2)
btnequal.grid(row=5,column=3)
btnplus.grid(row=4,column=3)





def btnClick(number):
  current=e.get() #nolasa esošo skaitli
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
    else:
        result=0
    e.delete(0,END)
    e.insert(0,str(result))
    return 0

def clear():
     e.delete(0,END)




# command=lambda:btnClick(0) #funkcijai padod parametrus


mansLogs.mainloop()