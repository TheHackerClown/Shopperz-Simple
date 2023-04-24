from tkinter import Tk, ttk,Text,filedialog, messagebox, END,Frame,StringVar,Toplevel
from cryptography.fernet import Fernet
import sv_ttk

#setup Instance
window = Tk()
window.iconbitmap('IMG_Data/bill.ico')
window.title('The Shopperz Bill Opener')
window.resizable(False,False)
frame = Frame(window).grid()

#text variables
global file
global passc
file = StringVar()
passc = StringVar()

#functions

global openFile
global wrtBil
def openFile():
    file.set("")
    ask = filedialog.askopenfilename(
        initialdir="Bills/",
        title='Open Sprz Bill File',
        filetypes =(('Shopperz Files (Secure)','*.sprz'),('All Files', '*.*'))
        )
    file.set(ask)
x= open('Bills/userdb.sprz', 'r')
userdb = x.readlines()
code = userdb[3]
user = userdb[1]
date_issue = userdb[2]
akey = open('Bills/userdb.sprz','rb')
key = akey.read(44)
def wrtBil(file):
    path = file.get()
    if passc.get() == code:
            bill_view = Toplevel()
            bill_view.title('Bill Viewer')
            bill_view.iconbitmap('IMG_Data/bill_assets/bill.ico')
            bill = Text(bill_view,height=25,width=45)
            bill.grid()
            with open(path,'rb') as file:
                content = file.read()
                bill_decrypted = Fernet(key).decrypt(content)
                bill.insert(END,bill_decrypted)
            bill.config(state='disabled')
    else:
            messagebox.showerror('Passcode Error', 'Password entered was wrong or not inputted correctly. Try Again!')
    passc.set("")


#frames
ttk.Label(frame,text='--Bill Details--').grid(row=0,column=1,pady = 5)

ttk.Label(frame,text='File Path').grid(row=1,column=1,pady = 5)

ttk.Label(frame,text='Passcode To Open').grid(row=2,column=1,pady = 5)

file_entry = ttk.Entry(frame,textvariable=file).grid(row=1,column=2,pady = 5)

passcode_entry = ttk.Entry(frame,show='*',textvariable=passc).grid(row=2,column=2,pady = 5)

file_button = ttk.Button(frame,text='-->',command=lambda: openFile()).grid(row=1,column=3,pady = 5,padx=5)

open_button = ttk.Button(frame,text='OPEN',command=lambda: wrtBil(file)).grid(row=3,column=2,pady = 5)

button = ttk.Button(frame, text="Toggle theme", command=sv_ttk.toggle_theme).grid(row=3,column=1,pady = 5)

ttk.Button(frame,text='About',command=lambda:messagebox.showinfo('About',f'Made by : TheHackerClown\nIssued : {date_issue}\nLicensed To : {user}')).grid(row=3,column=3,pady = 5,padx=5)


sv_ttk.set_theme('dark')
window.mainloop()
