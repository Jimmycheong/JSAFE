from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('700x700')
treeview = ttk.Treeview(root)
treeview.pack(fill=BOTH, expand=1)
treeview.insert('', '0', 'item1', text= 'First item')
treeview.insert('', '1', 'item2', text= 'Second item')
treeview.insert('', 'end', 'item3', text= 'Third item')
#treeview.detach('item1')


treeview.config(columns =('Username','hello'))

treeview.column('Username', width = 50, anchor = CENTER)
treeview.column('hello', width = 50, anchor = CENTER)


treeview.column('#0', width = 150)

treeview.heading('Username', text = 'Username')
treeview.heading('#0', text = 'Username')
treeview.heading('#0', text = 'Password')

treeview.set('item1', 'Username', 'Happy')
treeview.set('item2', 'Username', 'Sad')

def callback(event):
	print (treeview.selection())

treeview.bind('<<TreeviewSelect>>', callback)


root.mainloop()