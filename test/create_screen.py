from tkinter import * 
from tkinter import ttk 

def Main():
	
	class Local: 

		def __init__(self, master):

			master.title("Jimmy's password storage App")
			master.geometry('800x600+0+0')
			#master.geometry('600x700')
			master.minsize(600, 500)
			master.configure(background='grey')

			self.ccanvas = cCanvas(master, bg = 'grey')
			self.ccanvas.pack(fill=BOTH,expand =1)

			self.create_title = Label(self.ccanvas,text='JSAFE', foreground='white', bg='grey', font=('Arial', 24,'bold'))
			self.slogan = Label(self.ccanvas,text='Secure password storage', bg ='grey',foreground='white', font=('Arial', 12))
			self.create_title.place(relx=0.5, rely=0.2, anchor = CENTER)
			self.slogan.place(relx=0.5, rely=0.25, anchor = CENTER)

			self.compstring = Label(self.ccanvas, fg = 'white', bg = 'grey',text = 'Are you sure you wa *', font = ('Arial', 15))
			self.userstring = Label(self.ccanvas, fg = 'white', bg = 'grey',text = 'Username', font = ('Arial', 15))
			self.passstring = Label(self.ccanvas, fg = 'white', bg = 'grey',text = 'Password *', font = ('Arial', 15))
			self.notestring = Label(self.ccanvas, fg = 'red', bg = 'grey',text = '* = cumpulsory fields', font = ('Arial', 15))

			self.compentry = Entry(self.ccanvas, width = 20)
			self.userentry = Entry(self.ccanvas, width = 20)
			self.passwordentry = Entry(self.ccanvas, width = 20)

			self.compstring.place(relx=0.2, rely= 0.4, anchor = CENTER)
			self.userstring.place(relx=0.2, rely= 0.5, anchor = CENTER)
			self.passstring.place(relx=0.2, rely= 0.6, anchor = CENTER)
			self.compentry.place(relx=0.5, rely= 0.4, anchor = CENTER)
			self.userentry.place(relx=0.5, rely= 0.5, anchor = CENTER)
			self.passwordentry.place(relx=0.5, rely= 0.6, anchor = CENTER)
			self.notestring.place(relx=0.5, rely= 0.8, anchor = CENTER)

			#self.passentry.place(relx=0.5, rely= 0.5, y= 10, anchor =CENTER)

			self.passbutton = Button(self.ccanvas, text='Create')
			self.passbutton.place(relx = 0.5, rely=0.65, anchor = CENTER, y=50)





	root = Tk()
	my_app = Local(root)
	root.mainloop()

if __name__== '__main__':
	Main()
