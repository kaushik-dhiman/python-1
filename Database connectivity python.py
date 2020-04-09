from tkinter import *
import mysql.connector

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

Fullname=StringVar()
Email=StringVar()
Password=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()



def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   passw=Password.get()
   prog=var1.get()
   mydb = mysql.connector.connect(
   host="localhost",
   user="root",   
   passwd="",
   database="Student"
)
   cursor = mydb.cursor()
   val=(name1,email,passw,gender,country)
   sql="INSERT INTO Student (FullName,Email,Password,Gender,country) VALUES(%s,%s,%s,%s,%s)"
   cursor.execute(sql,val)
   mydb.commit()
   l1 = Label(root, text="Data Saved!",width=20,font=("bold", 8))
   l1.place(x=185,y=420)
   
   
             
label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Email)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Password",width=20,font=("bold", 10))
label_4.place(x=76,y=330)

entry_3 = Entry(root,textvar=Password)
entry_3.place(x=240,y=330)

Button(root, text='Submit',width=20,bg='black',fg='white',command=database).place(x=180,y=380)


root.mainloop()
