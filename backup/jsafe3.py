from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from Crypto.Cipher import AES 
from Crypto.Hash import SHA256 
from PIL import Image, ImageTk


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from jdb import Base, Epasswords

##===========##
#SESSION
##===========##
engine = create_engine('sqlite:///storage.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

allentries = session.query(Epasswords).all()


def Main():

	class Safe:

		def __init__(self, master): 

			master.title("Jimmy's password storage App")
			master.geometry('800x600+0+0')
			#master.geometry('600x700')
			master.minsize(600, 500)
			master.configure(background='grey')
			#master.resizable(False,False)

			#====#====##====#====##====#====##====#====#
			#INITIAL SCREEN 
			#====#====##====#====##====#====##====#====#
			self.firstframe = Frame(master, background = 'grey')
			#self.firstframe.pack(fill=BOTH, expand = 1) 


			self.passlabel = Label(self.firstframe, fg = 'white', bg = 'grey',text = 'Enter your password', font = ('Arial', 24, 'bold'))
			self.passlabel.place(relx=0.5, rely= 0.5, y=-50, anchor = CENTER)

			self.passentry = Entry(self.firstframe, width = 20, show = "*")
			self.passentry.place(relx=0.5, rely= 0.5, y= 10, anchor =CENTER)

			self.passbutton = Button(self.firstframe, text='Enter')
			self.passbutton.place(relx = 0.5, rely=0.5, anchor = CENTER, y=50)

			self.errormess = Label(self.firstframe, fg = 'red', bg = 'grey',text = 'Incorrect, please try again', font = ('Arial', 12))

			self.logolabel = Label(self.firstframe, background = 'grey')
			self.logolabel.place(relx=0.5, rely= 0.5, y=-120, anchor = CENTER)

			self.vault = ImageTk.PhotoImage(Image.open('img/lock.png').resize((70,70)))
			self.logolabel.configure(image = self.vault)

			def init_pass():
				print ('Enter button pressed!')
				if self.passentry.get() != 'hello': 
					self.passentry.delete(0,END)
					self.errormess.place(relx=0.5, rely= 0.5, y=90, anchor = CENTER)
				else: 
					self.firstframe.pack_forget()

			#====#====##====#====##====#====##====#====#
			#MAIN PROGRAM 
			#====#====##====#====##====#====##====#====#

			self.add_new = Button(self.firstframe, text = 'add new')
			self.delete_existing = Button(self.firstframe, text = 'delete')
			self.refresh_db = Button(self.firstframe, text = 'refresh')

			#====#====##====#====##====#====##====#====#
			#Second Frame
			#====#====##====#====##====#====##====#====#


			self.secondframe=Frame(root)#, background = 'grey')
			self.secondframe.pack(fill=BOTH,expand=1,padx=20,pady=20)

			self.tmenu = Frame(self.secondframe)
			self.tmenu.pack(fill=BOTH, expand=1,padx=20)

			self.title = Label(self.tmenu,text='JSAFE', foreground='black', font=('Arial', 24,'bold'),compound=RIGHT)
			self.slogan = Label(self.tmenu,text='Keep track of passwords in a secure way', foreground='black', font=('Arial', 12))
			self.title.place(relx=0.1, rely=0.1, anchor = 'nw')
			self.slogan.place(relx=0.1, rely=0.5, anchor = 'nw')

			#Buttons		
			style = ttk.Style()
			style.theme_use('aqua')
			style.configure('RB.TButton', compound=RIGHT,background='red')

			self.plusbutton = ttk.Button(self.tmenu, text="New  ",compound=RIGHT, command = lambda: create_button())
			self.plusbutton.place(relx=0.85, rely= 0.2, anchor = CENTER)
			self.editbutton = ttk.Button(self.tmenu, text='Edit',compound=RIGHT, command= lambda: edit_button())
			self.editbutton.place(relx=0.85, rely= 0.5, anchor = CENTER)
			self.minusbutton = ttk.Button(self.tmenu, text='Remove',compound=RIGHT, command = lambda: delete_button(""))
			self.minusbutton.place(relx=0.85, rely= 0.8, anchor = CENTER)

			self.logo = ImageTk.PhotoImage(Image.open('img/unlocked.png').resize((40,40)))
			self.plus = ImageTk.PhotoImage(Image.open('img/scratch_new.png').resize((20,20)))
			self.edit = ImageTk.PhotoImage(Image.open('img/pencil.png').resize((20,20)))
			self.minus = ImageTk.PhotoImage(Image.open('img/delete.png').resize((20,20)))

			self.title.configure(image = self.logo)
			self.plusbutton.configure(image = self.plus)
			self.editbutton.configure(image = self.edit)
			self.minusbutton.configure(image = self.minus)

			#TREEVIEW 
			self.treeview = ttk.Treeview(self.secondframe, columns=('usernamec','passwordc'))
			self.treeview.pack(fill=BOTH, expand=1, padx = 20)
			self.treeview.column('#0', width = 100, anchor = CENTER)
			self.treeview.column('usernamec', width = 100, anchor = CENTER)
			self.treeview.column('passwordc', width = 100, anchor = CENTER)
			
			self.treeview.heading('#0', text='Company')
			self.treeview.heading('usernamec', text='Username')
			self.treeview.heading('passwordc', text='Password')

			for a in allentries: 
				self.treeview.insert('','end', '{}'.format(a.company), text='{}'.format(a.company))				
				self.treeview.set('{}'.format(a.company), 'usernamec', '{}'.format(a.username))
				self.treeview.set('{}'.format(a.company), 'passwordc', '{}'.format(a.password))

			#BOTTOM MENU
			self.bmenu = Frame(self.secondframe)
			self.bmenu.pack(fill=BOTH, expand=1, padx=20)

			self.decrypt = ttk.Button(self.bmenu, text="Decrypt",compound=RIGHT,command = lambda : extract(self.shown))
			self.decrypt.place(relx=0.85, rely= 0.5, anchor = CENTER)

			self.debutton = ImageTk.PhotoImage(Image.open('img/unlock.png').resize((20,20)))
			self.decrypt.configure(image = self.debutton)


			self.shown = ttk.Entry(self.bmenu, width = 40)
			self.shown.place(relx = 0.35, rely=0.5, anchor=CENTER)


		#CALLBACKS & BINDS:

			def create_button(): 
				self.secondframe.pack_forget()
				self.ccanvas.pack(fill=BOTH,expand =1)

			def create_form():
				print('Clicked!')
				print (self.compentry.get())
				print (self.passwordentry.get())
				if len(self.compentry.get()) != 0 and len(self.passwordentry.get()) != 0:
					if self.compentry.get() not in allentries: 
						new = Epasswords(company= self.compentry.get(), username = self.userentry.get(),password=self.passwordentry.get())
						session.add(new)
						session.commit()			
						self.treeview.insert('','end', '{}'.format(new.company), text='{}'.format(new.company))				
						self.treeview.set('{}'.format(new.company), 'usernamec', '{}'.format(new.username))
						self.treeview.set('{}'.format(new.company), 'passwordc', '{}'.format(new.password))
						self.ccanvas.pack_forget()						
						self.secondframe.pack(fill=BOTH, expand=1)

			def edit_button(): 
				self.secondframe.pack_forget()
				self.ecanvas.pack(fill=BOTH,expand =1)

			def delete_button(event):
				#try: 
					dselected = str(self.treeview.selection()[0])
					print ('D: ', dselected)
					messagebox.askyesno(title = 'Removing {}'.format(dselected), message='Are you sure you want to remove {}?'.format(dselected))
					deleteit = session.query(Epasswords).filter_by(company=dselected)
					for d in deleteit: 
						print (d.company, d.username, d.password)
						session.delete(d)
						session.commit()
					self.treeview.detach(self.treeview.selection()[0])
				#except: 
				#	pass
			
			def current_selection(event):
				print ('Selected:', self.treeview.selection()[0])
				temp =  (self.treeview.selection()[0])
				print (self.treeview.set(temp, 'passwordc'))
				self.shown.delete(0,END)
				self.shown.insert(END, self.treeview.set(temp, 'passwordc'))

			self.treeview.bind('<<TreeviewSelect>>', current_selection)




			#style.configure('TEntry')
			def extract(entry): 
				#INSERT DECRYPTION CODE HERE
				pass

			self.firstframe.bind('<Return>', lambda e: init_pass())
			self.secondframe.bind('<BackSpace>', lambda e: delete_button(e))
			
			#self.secondframe.pack_forget()		

			#====#====##====#====##====#====##====#====#
			#ADD MENU
			#====#====##====#====##====#====##====#====#

			self.ccanvas = Canvas(master, bg = 'grey')
			#self.ccanvas.pack(fill=BOTH,expand =1)

			self.create_title = Label(self.ccanvas,text='JSAFE', foreground='white', bg='grey', font=('Arial', 24,'bold'))
			self.slogan = Label(self.ccanvas,text='Secure password storage', bg ='grey',foreground='white', font=('Arial', 12))
			self.create_title.place(relx=0.5, rely=0.2, anchor = CENTER)
			self.slogan.place(relx=0.5, rely=0.25, anchor = CENTER)

			self.compstring = Label(self.ccanvas, fg = 'white', bg = 'grey',text = 'Company *', font = ('Arial', 15))
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
			#self.notestring.place(relx=0.5, rely= 0.8, anchor = CENTER)

			self.passbutton = Button(self.ccanvas, text='Create', command = lambda: create_form())
			self.passbutton.place(relx = 0.5, rely=0.65, anchor = CENTER, y=50)
			#====#====##====#====##====#====##====#====#
			#EDIT MENU
			#====#====##====#====##====#====##====#====#
			
			#GHOST THE SELECTED COMPANIE'S INFORMATION in the text fields. 

			self.ecanvas = Canvas(master, bg = 'grey')
			#self.ecanvas.pack(fill=BOTH,expand =1)

			self.edit_title = Label(self.ecanvas,text='JSAFE', foreground='white', bg='grey', font=('Arial', 24,'bold'))
			self.slogan = Label(self.ecanvas,text='Secure password storage', bg ='grey',foreground='white', font=('Arial', 12))
			self.edit_title.place(relx=0.5, rely=0.2, anchor = CENTER)
			self.slogan.place(relx=0.5, rely=0.25, anchor = CENTER)

			self.ecompstring = Label(self.ecanvas, fg = 'white', bg = 'grey',text = 'Company *', font = ('Arial', 15))
			self.euserstring = Label(self.ecanvas, fg = 'white', bg = 'grey',text = 'Username', font = ('Arial', 15))
			self.epassstring = Label(self.ecanvas, fg = 'white', bg = 'grey',text = 'Password *', font = ('Arial', 15))
			self.enotestring = Label(self.ecanvas, fg = 'red', bg = 'grey',text = '* = cumpulsory fields', font = ('Arial', 15))

			self.ecompentry = Entry(self.ecanvas, width = 20)
			self.euserentry = Entry(self.ecanvas, width = 20)
			self.epasswordentry = Entry(self.ecanvas, width = 20)

			self.ecompstring.place(relx=0.2, rely= 0.4, anchor = CENTER)
			self.euserstring.place(relx=0.2, rely= 0.5, anchor = CENTER)
			self.epassstring.place(relx=0.2, rely= 0.6, anchor = CENTER)
			self.ecompentry.place(relx=0.5, rely= 0.4, anchor = CENTER)
			self.euserentry.place(relx=0.5, rely= 0.5, anchor = CENTER)
			self.epasswordentry.place(relx=0.5, rely= 0.6, anchor = CENTER)
			#self.notestring.place(relx=0.5, rely= 0.8, anchor = CENTER)

			self.epassbutton = Button(self.ecanvas, text='Create')
			self.epassbutton.place(relx = 0.5, rely=0.65, anchor = CENTER, y=50)

	root = Tk() 
	my_app = Safe(root)
	root.mainloop()

if __name__ == "__main__": 
	Main()
