from tkinter import *  # From tkinter import everything
from tkinter import messagebox
import json


window=Tk()  # To define tkinter
window.title("To Do list")  # To determine window's title
window.minsize(600,350)  # To determine window's size
window.config(bg="#B1C29E")  # To determine window's background color

# To create a text bg means: background color fg means: foreground color
title_text=Label(text="To Do List",bg="#B1C29E",fg="#FCE7C8",font=("Monospace",24,"bold"))
title_text.place(x=210,y=30)  # To determine text's location

date_text=Label(text="Date:",bg="#B1C29E",fg="#FCE7C8",font=("Monospace",18,"bold"))
date_text.place(x=120,y=120)

to_do_text=Label(text="To Do:",bg="#B1C29E",fg="#FCE7C8",font=("Monospace",18,"bold"))
to_do_text.place(x=105,y=170)

date_entry=Entry()  # to create an input
date_entry.config(width=30)  # To determine inout's width
date_entry.insert(0,"dd,mm,yyyy")  # To add input a default text
date_entry.place(x=200,y=130)  # To determine input's default location

to_do_entry=Entry()
to_do_entry.config(width=30)
to_do_entry.place(x=200,y=180)

def appending_text_to_file():
    date=date_entry.get()  
    to_do=to_do_entry.get()
    new_data={
        date:{
            "to do":to_do,
        }
    }

    if len(date)==0 or len(to_do)==0:
        # If inputs are empty then show a pop-up
        messagebox.showinfo(title="Ooopss",message="Please make sure you haven't left any fields empty")
    else: # If ınputs are not empty
        try:  # Try this code blocks
            # This path is special for my computer it won't work in your computer
            # I opened file r mode so reading mode
            with open("C:/Users/CASPER/Desktop/python_projects/To Do list/data.json","r") as data_file:
                data=json.load(data_file)  # data_file being read and converted to the python file(list,dict)
        except FileNotFoundError:  # If you see FileNOtFoundEror
                # Open this path w mode so writing mode
                # This path is special for my computer it won't work in your computer
                with open("C:/Users/CASPER/Desktop/python_projects/To Do list/data.json","w") as data_file:
                    json.dump(new_data,data_file,indent=4)  # Converted that file to json file
        else:   # If you don't see that eror
                data.update(new_data) #update data to new_data
                with open("C:/Users/CASPER/Desktop/python_projects/To Do list/data.json","w") as data_file:
                    json.dump(data,data_file,indent=4)

        finally:
                # To clear all inputs 
                date_entry.delete(0,END)
                to_do_entry.delete(0,END)
                

# To create a button
generate_buton=Button(text="Generate",bg="#B1C29E",width=30,command=appending_text_to_file)
generate_buton.place(x=170,y=220)



def search():
    date=date_entry.get()
    try:  
        with open("C:/Users/CASPER/Desktop/python_projects/To Do list/data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:  
            messagebox.showinfo(title="Eror",message="No Data File Found")  # Show a pop_up in the screen
    else:  # If you don't see that  error
        if date in data:
            to_do_show=data[date]["to do"]
            messagebox.showinfo(title="Do To",message=f"Date: {date}\nto do: {to_do_show}")
        else:
            messagebox.showinfo(title="Eror",message=f"No details for {date} exists")

     
search_buton=Button(text="Search",bg="#B1C29E",width=15,command=search)
search_buton.place(x=420,y=125)


window.mainloop()  # If I don't click exit buton the screen won't close