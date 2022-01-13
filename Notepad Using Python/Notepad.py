import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad:

	__root__ = Tk()

	# default window width and height
	__thisWidth__ = 300
	__thisHeight__ = 300
	__thisTextArea__ = Text(__root__)
	__thisMenuBar__ = Menu(__root__)
	__thisFileMenu__ = Menu(__thisMenuBar__, tearoff=0)
	__thisEditMenu__ = Menu(__thisMenuBar__, tearoff=0)
	__thisHelpMenu__ = Menu(__thisMenuBar__, tearoff=0)
	
	# To add scrollbar
	__thisScrollBar__ = Scrollbar(__thisTextArea__)	
	__file__ = None

	def __init__(self,**kwargs):

		# Set icon
		try:
				self.__root__.wm_iconbitmap("Notepad.ico")
		except:
				pass

		# Set window size (the default is 300x300)

		try:
			self.__thisWidth__ = kwargs['width']
		except KeyError:
			pass

		try:
			self.__thisHeight__ = kwargs['height']
		except KeyError:
			pass

		# Set the window text
		self.__root__.title("Untitled - Notepad")

		# Center the window
		screenWidth = self.__root__.winfo_screenwidth()
		screenHeight = self.__root__.winfo_screenheight()
	
		# For left-align
		left = (screenWidth / 2) - (self.__thisWidth__ / 2)
		
		# For right-align
		top = (screenHeight / 2) - (self.__thisHeight__ /2)
		
		# For top and bottom
		self.__root__.geometry('%dx%d+%d+%d' % (self.__thisWidth__,
											self.__thisHeight__,
											left, top))

		# To make the textarea auto resizable
		self.__root__.grid_rowconfigure(0, weight=1)
		self.__root__.grid_columnconfigure(0, weight=1)

		# Add controls (widget)
		self.__thisTextArea__.grid(sticky = N + E + S + W)
		
		# To open new file
		self.__thisFileMenu__.add_command(label="New",
										command=self.__newFile)
		
		# To open a already existing file
		self.__thisFileMenu__.add_command(label="Open",
										command=self.__openFile)
		
		# To save current file
		self.__thisFileMenu__.add_command(label="Save",
										command=self.__saveFile)

		# To create a line in the dialog	
		self.__thisFileMenu__.add_separator()										
		self.__thisFileMenu__.add_command(label="Exit",
										command=self.__quitApplication)
		self.__thisMenuBar__.add_cascade(label="File",
									menu=self.__thisFileMenu__)	
		
		# To give a feature of cut
		self.__thisEditMenu__.add_command(label="Cut",
										command=self.__cut)			
	
		# to give a feature of copy
		self.__thisEditMenu__.add_command(label="Copy",
										command=self.__copy)		
		
		# To give a feature of paste
		self.__thisEditMenu__.add_command(label="Paste",
										command=self.__paste)		
		
		# To give a feature of editing
		self.__thisMenuBar__.add_cascade(label="Edit",
									menu=self.__thisEditMenu__)	
		
		# To create a feature of description of the notepad
		self.__thisHelpMenu__.add_command(label="About Notepad",
										command=self.__showAbout)
		self.__thisMenuBar__.add_cascade(label="Help",
									menu=self.__thisHelpMenu__)

		self.__root__.config(menu=self.__thisMenuBar__)

		self.__thisScrollBar__.pack(side=RIGHT,fill=Y)				
		
		# Scrollbar will adjust automatically according to the content	
		self.__thisScrollBar__.config(command=self.__thisTextArea__.yview)	
		self.__thisTextArea__.config(yscrollcommand=self.__thisScrollBar__.set)
	
		
	def __quitApplication(self):
		self.__root__.destroy()
		# exit()

	def __showAbout(self):
		showinfo("Notepad","Designed by tulaskaratul.")

	def __openFile(self):
		
		self.__file__ = askopenfilename(defaultextension=".txt",
									filetypes=[("All Files","*.*"),
										("Text Documents","*.txt")])

		if self.__file__ == "":
			
			# no file to open
			self.__file__ = None
		else:
			
			# Try to open the file
			# set the window title
			self.__root__.title(os.path.basename(self.__file__) + " - Notepad")
			self.__thisTextArea__.delete(1.0,END)

			file = open(self.__file__,"r")

			self.__thisTextArea__.insert(1.0,file.read())

			file.close()

		
	def __newFile(self):
		self.__root__.title("Untitled - Notepad")
		self.__file__ = None
		self.__thisTextArea__.delete(1.0,END)

	def __saveFile(self):

		if self.__file__ == None:
			# Save as new file
			self.__file__ = asksaveasfilename(initialfile='Untitled.txt',
											defaultextension=".txt",
											filetypes=[("All Files","*.*"),
												("Text Documents","*.txt")])

			if self.__file__ == "":
				self.__file__ = None
			else:
				
				# Try to save the file
				file = open(self.__file__,"w")
				file.write(self.__thisTextArea__.get(1.0,END))
				file.close()
				
				# Change the window title
				self.__root__.title(os.path.basename(self.__file__) + " - Notepad")
				
			
		else:
			file = open(self.__file__,"w")
			file.write(self.__thisTextArea__.get(1.0,END))
			file.close()

	def __cut(self):
		self.__thisTextArea__.event_generate("<<Cut>>")

	def __copy(self):
		self.__thisTextArea__.event_generate("<<Copy>>")

	def __paste(self):
		self.__thisTextArea__.event_generate("<<Paste>>")

	def run(self):

		# Run main application
		self.__root__.mainloop()




# Run main application
notepad = Notepad(width=600,height=400)
notepad.run()
