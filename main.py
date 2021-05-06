import mysql.connector as mysql
from tkinter import *
import tkinter.messagebox as MessageBox

HOST_DB = "localhost"
USER_DB = "root"
PASSWORD = ""
DATABASE = "dev_team"


def insert():
    id = e_id.get()
    name = e_name.get()

    if id == "" or name == "":
        MessageBox.showinfo("Insert Status", "All Fields are required")

    else:
        con = mysql.connect(host=HOST_DB, user=USER_DB, password=PASSWORD, database=DATABASE)
        cursor = con.cursor()
        cursor.execute("insert into developers  values('" + id + "', '" + name + "')")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, "end")
        show()
        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()


def delete():
    if e_id.get() == "":
        MessageBox.showinfo("Delete Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host=HOST_DB, user=USER_DB, password=PASSWORD, database=DATABASE)
        cursor = con.cursor()
        cursor.execute("delete from developers  where developer_id='" + e_id.get() + "'")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, "end")
        show()
        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()


def update():
    id = e_id.get()
    name = e_name.get()

    if id == "" or name == "":
        MessageBox.showinfo("Update Status", "All Fields are required")

    else:
        con = mysql.connect(host=HOST_DB, user=USER_DB, password=PASSWORD, database=DATABASE)
        cursor = con.cursor()
        cursor.execute("update developers  set developer_name '" + name + "' where developer_id='" + id + "'")
        cursor.execute("commit")

        e_id.delete(0, 'end')
        e_name.delete(0, "end")
        show()
        MessageBox.showinfo("Update Status", "Updated Successfully")
        con.close()


def get():
    if e_id.get() == "":
        MessageBox.showinfo("Fetch Status", "ID is compolsary for delete")
    else:
        con = mysql.connect(host=HOST_DB, user=USER_DB, password=PASSWORD, database=DATABASE)
        cursor = con.cursor()
        cursor.execute("select * from developers  where developer_id='" + e_id.get() + "'")
        rows = cursor.fetchall()

        for row in rows:
            e_name.insert(0, row[1])

        con.close()


def show():
    con = mysql.connect(host=HOST_DB, user=USER_DB, password=PASSWORD, database=DATABASE)
    cursor = con.cursor()
    cursor.execute("select * from developers ")
    rows = cursor.fetchall()
    list.delete(0, list.size())
    for row in rows:
        insertData = str(row[0]) + '    ' + row[1]
        list.insert(list.size() + 1, insertData)
    con.close()


root = Tk()
root.geometry("600x300")
root.title("DB Master")

id = Label(root, text="Enter developer ID", font=('bold', 10))
id.place(x=20, y=30)

dev_name = Label(root, text="Enter developer name", font=('bold', 10))
dev_name.place(x=20, y=60)

e_id = Entry()
e_id.place(x=150, y=30)

e_name = Entry()
e_name.place(x=150, y=60)

insert = Button(root, text="Insert", font=("italic", 10), bg="white", command=insert)
insert.place(x=20, y=140)

delete = Button(root, text="Delete", font=("italic", 10), bg="white", command=delete)
delete.place(x=70, y=140)

update = Button(root, text="Update", font=("italic", 10), bg="white", command=update)
update.place(x=130, y=140)

get = Button(root, text="Get", font=("italic", 10), bg="white", command=get)
get.place(x=190, y=140)

list = Listbox(root)
list.place(x=290, y=30)
show()

root.mainloop()
