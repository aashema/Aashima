from tkinter import *
import backend
def clear():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
def add_command():
    backend.insert(title_text.get(),
                   author_text.get(),
                   year_text.get(),
                   isbn_text.get())
    listing.delete(0,END)
    listing.insert(END,
                   (title_text.get(),
                   author_text.get(),
                   year_text.get(),
                   isbn_text.get()))
    clear()
def view_command():
    listing.delete(0,END)
    for row in backend.view():
        listing.insert(END,row)
def update_command():
    backend.update(selected_tuple[0],
                   title_text.get(),
                   author_text.get(),
                   year_text.get(),
                   isbn_text.get())
def delete_command():
    backend.delete(selected_tuple[0])
    clear()
    view_command()
def search_command():
    listing.delete(0,END)
    for row in backend.search(title_text.get(),
                              author_text.get(),
                              year_text.get(),
                              isbn_text.get()):
        listing.insert(END,row)

def get_selected_row(event):
    try:
        global selected_tuple
        index=listing.curselection()[0]
        selected_tuple=listing.get(index)
        entry1.delete(0,END)
        entry1.insert(END,selected_tuple[1])
        entry2.delete(0,END)
        entry2.insert(END,selected_tuple[2])
        entry3.delete(0,END)
        entry3.insert(END,selected_tuple[3])
        entry4.delete(0,END)
        entry4.insert(END,selected_tuple[4])
    except:
        pass
window=Tk()
window.title("LIBRARY MANAGEMENT SYSTEM")
label1=Label(window,text="Title",bg="blue",fg="white",font="Times 15 bold",relief=RAISED,bd=4)
label1.grid(row=0,column=0,padx=5,pady=5,sticky='nswe')
label2=Label(window,text="Author",bg="blue",fg="white",font="Times 15 bold",relief=RAISED,bd=4)
label2.grid(row=0,column=2,padx=5,pady=5,sticky='nswe')
label3=Label(window,text="Year",bg="blue",fg="white",font="Times 15 bold",relief=RAISED,bd=4)
label3.grid(row=1,column=0,padx=5,pady=5,sticky='nswe')
label4=Label(window,text="ISBN",bg="blue",fg="white",font="Times 15 bold",relief=RAISED,bd=4)
label4.grid(row=1,column=2,padx=5,pady=5,sticky='nswe')


title_text=StringVar()
entry1=Entry(window,textvariable=title_text,bg="blue",fg="white",font="Times 15 bold",relief=RAISED,bd=4)
entry1.grid(row=0,column=1,padx=5,pady=5,sticky='nswe')
author_text=StringVar()
entry2=Entry(window,textvariable=author_text,bg="blue",fg="white",font="Times 15 bold",relief=RAISED,bd=4)
entry2.grid(row=0,column=3,padx=5,pady=5,sticky='nswe')
year_text=StringVar()
entry3=Entry(window,textvariable=year_text,bg="blue",fg="white",font="Times 15 bold",relief=RAISED,bd=4)
entry3.grid(row=1,column=1,padx=5,pady=5,sticky='nswe')
isbn_text=StringVar()
entry4=Entry(window,textvariable=isbn_text,bg="blue",fg="white",font="Times 15 bold",relief=RAISED,bd=4)
entry4.grid(row=1,column=3,padx=5,pady=5,sticky='nswe')

listing=Listbox(window,height=16,width=35,bg='black',fg='white',font="Times 15 bold")
listing.grid(row=2,column=0,rowspan=6,padx=5,pady=5,columnspan=3,sticky='nswe')
listing.bind('<<ListboxSelect>>',get_selected_row)

button1=Button(window,text="View All",width=12,command=view_command,bg="blue",fg="white",font="Times 15 bold")
button1.grid(row=2,column=3,pady=5,sticky='nswe')

button2=Button(window,text="Search Entry",width=12,command=search_command,bg="blue",fg="white",font="Times 15 bold")
button2.grid(row=3,column=3,pady=5,sticky='nswe')

button3=Button(window,text="Add Entry",width=12,command=add_command,bg="blue",fg="white",font="Times 15 bold")
button3.grid(row=4,column=3,pady=5,sticky='nswe')

button4=Button(window,text="Update Selected",width=12,command=update_command,bg="blue",fg="white",font="Times 15 bold")
button4.grid(row=5,column=3,pady=5,sticky='nswe')

button5=Button(window,text="Delete Selected",width=12,command=delete_command,bg="blue",fg="white",font="Times 15 bold")
button5.grid(row=6,column=3,pady=5,sticky='nswe')

button6=Button(window,text="Close",width=12,command=window.destroy,bg="blue",fg="white",font="Times 15 bold")
button6.grid(row=7,column=3,pady=5,sticky='nswe')
for i in range(8):
    window.grid_rowconfigure(i,weight=1)
for i in range(4):
    window.grid_columnconfigure(i,weight=1)
window.mainloop()                
               
                
                
                   
                   
