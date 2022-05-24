from tkinter import *
import csv
from tkinter import messagebox

books = []
def ReadCSVFile():
	global header
	with open('BooksData.csv') as csvfile:
		csv_reader = csv.reader(csvfile,delimiter=',')
		header = next(csv_reader)
		for row in csv_reader:
			books.append(row)
	set_select()		
	print(books)

def WriteInCSVFile(books):
	with open('BooksData.csv','w',newline='') as csv_file:
		writeobj = csv.writer(csv_file,delimiter=',')
		writeobj.writerow(header)
		for row in books:
			writeobj.writerow(row)


def WhichSelected():
	print(" ",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error", "Please Select the Book Name")
	else:
		return int(select.curselection()[0])
		


def AddDetail():
	if E_book_name.get()!="" and E_author.get()!="" and E_pub_year.get()!="" and E_price.get()!="":
		books.append([E_book_name.get(),E_author.get(),E_pub_year.get(),E_price.get()])
		print(books)
		WriteInCSVFile(books)
		set_select()
		EntryReset()
		messagebox.showinfo("Confirmation", "Succesfully added new book")
		
	else:
		messagebox.showerror("Error", "Please fill the information")

def UpdateDetail():
	if E_book_name.get() and E_author.get() and E_pub_year.get() and E_price.get():
		books[WhichSelected()] = [ E_book_name.get(), E_author.get(), E_pub_year.get(), E_price.get()]
		WriteInCSVFile(books)
		messagebox.showinfo("Confirmation", "Succesfully Updated Book")
		EntryReset()
		set_select()
	elif not(E_book_name.get()) and not(E_author.get()) and not(E_pub_year.get()) and not(E_pub_year.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Please fill the information")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please select the book name and \n press Load button")
		else:
			message1 = """To Load the all information of \n 
						  selected row press Load button\n.
						  """
			messagebox.showerror("Error", message1)

def EntryReset():
	E_book_name_var.set('')
	E_author_var.set('')
	E_pub_year_var.set('')
	E_price_var.set('')


def DeleteEntry():
	if len(select.curselection())!=0:
		result=messagebox.askyesno('Confirmation','You Want to Delete Book\n Which you selected')
		if result==True:
			del books[WhichSelected()]
			WriteInCSVFile(books)
			set_select()
	else:
		messagebox.showerror("Error", 'Please select the Book')

def LoadEntry():
    book_name, author, pub_year, price = books[WhichSelected()]
    E_book_name_var.set(book_name)
    E_author_var.set(author)
    E_pub_year_var.set(pub_year)
    E_price_var.set(price)


def set_select():
    books.sort(key=lambda record: record[0])
    select.delete(0, END)
    i=0
    for book_name, author, pub_year, price in books:
    	i+=1
    	select.insert(END, f"{i}  |    {book_name}   |    {author}   |   {pub_year}|   {price}")


window = Tk()

window.title('Book Resell')

Frame1 = LabelFrame(window,text="Enter the Book Details")
Frame1.grid(padx=15,pady=15)


Inside_Frame1 = Frame(Frame1)
Inside_Frame1.grid(row=0,column=0,padx=15,pady=15)
#---------------------------------------------
l_book_name = Label(Inside_Frame1,text="Book Name")
l_book_name.grid(row=0,column=0,padx=5,pady=5)
E_book_name_var = StringVar()

E_book_name = Entry(Inside_Frame1,width=30, textvariable=E_book_name_var)
E_book_name.grid(row=0,column=1,padx=5,pady=5)
#-----------------------------------------------
l_author= Label(Inside_Frame1,text="Author")
l_author.grid(row=1,column=0,padx=5,pady=5)
E_author_var= StringVar()
E_author = Entry(Inside_Frame1,width=30,textvariable=E_author_var)
E_author.grid(row=1,column=1,padx=5,pady=5)
#---------------------------------------------------
l_pub_year= Label(Inside_Frame1,text="Pub_year")
l_pub_year.grid(row=2,column=0,padx=5,pady=5)
E_pub_year_var = StringVar()
E_pub_year = Entry(Inside_Frame1,width=30,textvariable=E_pub_year_var)
E_pub_year.grid(row=2,column=1,padx=5,pady=5)
#---------------------------------------------------
l_price= Label(Inside_Frame1,text="Price")
l_price.grid(row=3,column=0,padx=5,pady=5)
E_price_var = StringVar()
E_price = Entry(Inside_Frame1,width=30,textvariable=E_price_var)
E_price.grid(row=3,column=1,padx=5,pady=5)
#---------------------------------------------------
Frame2 = Frame(window)
Frame2.grid(row=0,column=1,padx=15,pady=15,sticky=E)
#<><><><><><><><><><><><><><<><<<><><<<><><><><><><><><><>
Add_button = Button(Frame2,text="Add Detail",width=15,bg="#6B69D6",fg="#FFFFFF",command=AddDetail)
Add_button.grid(row=0,column=0,padx=8,pady=8)

Update_button = Button(Frame2,text="Update Detail",width=15,bg="#6B69D6",fg="#FFFFFF",command=UpdateDetail)
Update_button.grid(row=1,column=0,padx=8,pady=8)


Reset_button = Button(Frame2,text="Reset",width=15,bg="#6B69D6",fg="#FFFFFF",command=EntryReset)
Reset_button.grid(row=2,column=0,padx=8,pady=8)
#----------------------------------------------------------------------------

DisplayFrame = Frame(window)
DisplayFrame.grid(row=1,column=0,padx=15,pady=15)

scroll = Scrollbar(DisplayFrame, orient=VERTICAL)
select = Listbox(DisplayFrame, yscrollcommand=scroll.set,font=("Arial Bold",10),bg="#282923",fg="#E7C855",width=40,height=10,borderwidth=3,relief="groove")
scroll.config(command=select.yview)
select.grid(row=0,column=0,sticky=W)
scroll.grid(row=0,column=1,sticky=N+S)



#-----------------------------------------------------------------------------------
ActionFrame = Frame(window)
ActionFrame.grid(row=1,column=1,padx=15,pady=15,sticky=E)

Delete_button = Button(ActionFrame,text="Delete",width=15,bg="#D20000",fg="#FFFFFF",command=DeleteEntry)
Delete_button.grid(row=0,column=0,padx=5,pady=5,sticky=S)

Loadbutton = Button(ActionFrame,text="Load",width=15,bg="#6B69D6",fg="#FFFFFF",command=LoadEntry)
Loadbutton.grid(row=1,column=0,padx=5,pady=5)
#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx





ReadCSVFile()


	

window.mainloop()
