import bs4
import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def url_scrap(url):
    try:
        result = requests.get(url)
        soup = bs4.BeautifulSoup(result.text, 'lxml')
        images = soup.select('img')
        """for img in images:
            print(img['src'])"""
        return images
    except:
        return ""

def process_url():
    try:
        entered_url = url.get()
        images = url_scrap(entered_url)
        return images
    except:
        return ""

def command_button():
    try: 
        urls = ""
        urls = process_url()
        if len(urls) <= 0:
            messagebox.showinfo("Message", "Insert an url inside of the box")
        else:
            for i, url in enumerate(urls, start=1):
                tree.insert(parent="", index = "end", iid=i, text=str(i), values=(url['src'],))
        reset()
        disabled_button()
    except:
        messagebox.showinfo("Message", "Insert an url inside of the box")
        reset()

def reset():
    url.delete(0, END)

def clean():
    reset()
    tree.delete(*tree.get_children())
    enable_button()

def disabled_button():
    button_url.config(state='disabled')
    

def enable_button():
    button_url.config(state='normal')
    
        
#Extraer el titulo
# print(soup.select('title')[0].get_text())
# Tkinter innit
app = Tk()
#zise of windowd
app.geometry('1020x630')

#evitar maximizar
app.resizable(0,0)

#title of window
app.title("WebScrapper")

#background of th windowd
app.config(bg='burlywood')

#superioir display
display_top = Frame(app, bd=1, relief= FLAT)
display_top.pack(side=TOP)

#label title
label_Title= Label(display_top, text='WebScrapper', fg='azure4', font=('Dosis',25), bg='burlywood', width=27)
label_Title.grid(row=0, column=0)

#mid display
display_left = Frame(app,bd=1, relief=FLAT)
display_left.pack(side=LEFT)

#label of buttons left
label_url = Label(display_left, text='Url')
label_url.grid(row=0, column=0)

#Entry of url
url = Entry(display_left)
url.grid(row=1, column=0)

#Button of the url
button_url = Button(display_left,text="Check", command=command_button)
button_url.grid(row=2, column=0)

#bUTTON OF ERRASER
button_clean = Button(display_left, text="Clean", command=clean)
button_clean.grid(row=3,column=0)

#mid display
display_right = Frame(app,bd=1,relief=FLAT)
display_right.pack(side=RIGHT)

#treeview
tree = ttk.Treeview(display_right)
tree["columns"] = ("URL")
tree.column("#0", width=100)
tree.column("URL", width=400)
tree.heading("#0", text="ID")
tree.heading("URL", text="URL")
tree.pack()



#Aclaracion para que no se cierre 
app.mainloop()