from tkinter import *

root = Tk()
root.title('Calculator')
e = Entry(root)
e.grid(row=0,column=0,columnspan=3,padx=20,pady=10)

eq=[]

def b_add(number):
	eq.append(number)
	current=e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))
	print(eq)
	

eq=[]

def b_plus(sign):
	eq.append(sign)
	e.delete(0,END)
	e.insert(0,str(sign))

def b_clear():
	eq.clear()
	e.delete(0,END)

def b_res():
	e.delete(0,END)
	re=''
	print(eq)
	for char in eq:
		re=re+str(char)
	print('valeur string: '+ re)
	res=eval(re)
	print(res)
	print(res)
	e.insert(0,res)

myButton1=Button(root,text='1',padx =20, pady =10,command = lambda : b_add(1))
myButton2=Button(root,text='2',padx =20, pady =10,command = lambda : b_add(2))
myButton3=Button(root,text='3',padx =20, pady =10,command = lambda : b_add(3))
myButton4=Button(root,text='4',padx =20, pady =10,command = lambda : b_add(4))
myButton5=Button(root,text='5',padx =20, pady =10,command = lambda : b_add(5))
myButton6=Button(root,text='6',padx =20, pady =10,command = lambda : b_add(6))
myButton7=Button(root,text='7',padx =20, pady =10,command = lambda : b_add(7))
myButton8=Button(root,text='8',padx =20, pady =10,command = lambda : b_add(8))
myButton9=Button(root,text='9',padx =20, pady =10,command = lambda : b_add(9))
myButton0=Button(root,text='9',padx =20, pady =10,command = lambda : b_add(0))

myButtonadd=Button(root,text='+',padx =20, pady =10,command = lambda : b_plus('+'))
myButtonminus=Button(root,text='-',padx =20, pady =10,command = lambda : b_plus('-'))
myButtonclear=Button(root,text='C',padx =20, pady =10,command = b_clear)
myButtonequal=Button(root,text='=',padx=20,pady =10,command = b_res)
myButtonper=Button(root,text='*',padx=20,pady=10,command = lambda : b_plus('*'))

myButton1.grid(row=4,column=0)
myButton2.grid(row=4,column=1)
myButton3.grid(row=4,column=2)

myButton4.grid(row=3,column=0)
myButton5.grid(row=3,column=1)
myButton6.grid(row=3,column=2)

myButton7.grid(row=2,column=0)
myButton8.grid(row=2,column=1)
myButton9.grid(row=2,column=2)

myButtonadd.grid(row=1,column=0)
myButtonminus.grid(row=1,column=1)
myButtonper.grid(row=5,column=0)
myButtonclear.grid(row=1,column=2)
myButtonequal.grid(row=5,column=0,columnspan=3)
root.mainloop()