from tkinter import * 
from tkinter import ttk
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
			master.geometry('800x600+100+100')
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

			self.plusbutton = ttk.Button(self.tmenu, text="Add New",compound=RIGHT)
			self.plusbutton.place(relx=0.85, rely= 0.2, anchor = CENTER)
			self.editbutton = ttk.Button(self.tmenu, text='Edit',compound=RIGHT)
			self.editbutton.place(relx=0.85, rely= 0.5, anchor = CENTER)
			self.minusbutton = ttk.Button(self.tmenu, text='Remove',compound=RIGHT)
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
			#style.configure('TEntry')

			self.bmenu = Frame(self.secondframe)
			self.bmenu.pack(fill=BOTH, expand=1, padx=20)

			self.decrypt = ttk.Button(self.bmenu, text="Decrypt",compound=RIGHT)
			self.decrypt.place(relx=0.85, rely= 0.5, anchor = CENTER)

			self.debutton = ImageTk.PhotoImage(Image.open('img/unlock.png').resize((20,20)))
			self.decrypt.configure(image = self.debutton)

			self.shown = ttk.Entry(self.bmenu, width = 40, state=['disabled'])
			self.shown.place(relx = 0.35, rely=0.5, anchor=CENTER)


		#BINDS:
			master.bind('<Return>', lambda e: init_pass())
			

	root = Tk() 
	my_app = Safe(root)
	root.mainloop()

if __name__ == "__main__": 
	Main()
