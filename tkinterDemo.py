from tkinter import *
import mysql.connector
import  tkinter.messagebox as msg


def  create_conn():
    return mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="python"
            )

def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert status","All Fields are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        quary="Insert into student(fname,lname,email,mobile) VALUES (%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(quary,args)
        conn.commit()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Insert status","Data Inserted Successfully") 
        conn.close()


root=Tk()
root.geometry("330x370")
root.title("My Tkinter Example")
root.resizable (width=False,height=False)

l_id=Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname=Label(root,text="First Name")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="Last Name")
l_lname.place(x=50,y=150)

l_email=Label(root,text="Email")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="Mobile")
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("Arial Black",10),command=insert_data) 
insert.place(x=20,y=300)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("Arial Black",10) )
search.place(x=90,y=300)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Arial Black",10) )
update.place(x=166,y=300)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Arial Black",10))
delete.place(x=241,y=300)
