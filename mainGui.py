from tkinter import Text,messagebox,ttk,Tk,StringVar,IntVar,END
import random
from PIL import ImageTk, Image
from cryptography.fernet import Fernet
import sv_ttk
import os
import webbrowser

#Load menu
splash_root = Tk()
splash_root.title('Loading.....')
splash_root.iconbitmap('IMG_Data/shopperz.ico')
img = ImageTk.PhotoImage(Image.open("IMG_Data/splash.png"))
label = ttk.Label(splash_root, image = img)
label.pack()
def main():
    splash_root.destroy()
splash_root.after(2000,main)
splash_root.mainloop()


#SETUP INSTANCE
sprz = Tk()
sprz.title('The Shopperz')
sprz.iconbitmap('IMG_Data/shopperz.ico')
sprz.resizable(False, False)


#main frames
master_frame = ttk.Frame(sprz)
master_frame.grid(row=0,column=1)

txt_frame = ttk.Frame(sprz,relief='solid',borderwidth=10)
txt_frame.grid(row=0,column=0)


#follow me on instagram for more updates
frame4 = ttk.LabelFrame(master_frame,text='More.....')
frame4.grid(row=0,column=1,padx=10,pady=5)
ttk.Button(frame4,text='Explore \nMore',command=lambda:webbrowser.open('https://www.github.com/TheHackerClown')).grid(padx=10,pady=10)

#Setting Item area
textarea = Text(txt_frame, width=45, height=23)
textarea.grid(row = 0, column=0)
textarea.insert(END, '=============================================')
textarea.insert(END, '\nArticle_Name\t|\tQuantity\t | Rate [Of 1 Item]')
textarea.insert(END, '\n=============================================')
textarea.config(state='disabled')
#textarea.insert(tk.END, 'macroni \t\t 2 \t\t 200')

#Variables
name = StringVar()
phone = IntVar()
item_name = StringVar()
quantity = IntVar()
rate = IntVar()
paymentinfo = StringVar()
paymentinfos = ('-----None-----',
		'💳 Paytm/Other UPI 💳',
		'💰      Cash      💰',
		)
paymentinfo.set(paymentinfos[0])
rate_of_items = []
keyfile = open('Bills/userdb.sprz','rb')
akey = keyfile.read(44)
userdb = open('Bills/userdb.sprz','r')
datalist = userdb.readlines()
user = datalist[1]
date_issue = datalist[2]

#functions

def generate():
    if os.path.exists('Bills/Bill Number Generator/UsedBillNumber.txt'):
        pass
    else:
        open('Bills/Bill Number Generator/UsedBillNumber.txt','x')
    usedbillwriter = open('Bills/Bill Number Generator/UsedBillNumber.txt', 'a')
    usedbillnumbers = open('Bills/Bill Number Generator/UsedBillNumber.txt', 'r')
    x = 0
    while x==0:
        x = random.randint(1000, 9999)
        if x in usedbillnumbers:
            continue
        else:
            usedbillwriter.write(str(x)+'\n')
            break
    return str(x)




#customer details
frame2 = ttk.LabelFrame(master_frame, text='Customer Details',padding=5)
frame2.grid(row=0,column=0,padx=10,pady=5)
ttk.Label(frame2, text='Name:            ').grid(row=0, column=0,pady=5,padx=5)
ttk.Entry(frame2, textvariable=name,width=20).grid(row=0, column=1,pady=5,padx=5)
ttk.Label(frame2, text='Phone No.:       ').grid(row=1, column=0,pady=5,padx=5)
ttk.Entry(frame2, textvariable=phone,width=20).grid(row=1, column=1,pady=5,padx=5)
ttk.Label(frame2, text='Payment Done In: ').grid(row=2,column=0,pady=5,padx=5)
ttk.OptionMenu(frame2, paymentinfo, *paymentinfos).grid(row=2,column=1,pady=5,padx=5)

#article details
frame3 = ttk.LabelFrame(master_frame, text='Article Details')
frame3.grid(row=1,column=1,padx=10,pady=5)
ttk.Label(frame3, text='Article Name: ').grid(row=0, column=0,pady=5,padx=5)
item_name_entry = ttk.Entry(frame3, textvariable=item_name,width=20).grid(row=0, column=1,pady=5,padx=5)
quantity_entry = ttk.Label(frame3, text='Quantity:     ').grid(row=1, column=0,pady=5,padx=5)
ttk.Entry(frame3, textvariable=quantity,width=20).grid(row=1, column=1,pady=5,padx=5)
ttk.Label(frame3, text='Rate:         ').grid(row=2, column=0,pady=5,padx=5)
rate_entry = ttk.Entry(frame3, textvariable=rate,width=20).grid(row=2, column=1,pady=5,padx=5)

#lots of buttons
def mkebil(rate_entry,quantity_entry,item_name_entry):
	n=int(rate_entry.get())
	m=int(quantity_entry.get())
	mm = (quantity_entry.get())*n
	l=item_name_entry.get()
	rate_of_items.append(mm)
	if l!='':
			textarea.config(state='normal')
			textarea.insert(END, f'\n{l} \t\t  {m}  \t\t {n}\n')
			textarea.config(state='disabled')
			rate_entry.set(0)
			quantity_entry.set(0)
			item_name_entry.set('')
	else:
		messagebox.showinfo('Error_404','No Item Inputed')

def clr():
	name.set('')
	phone.set(0)
	item_name.set('')
	rate.set(0)
	quantity.set(0)
	textarea.config(state='normal')
	textarea.delete("1.0",END)
	paymentinfo.set(paymentinfos[0])
	rate_of_items.clear()
	textarea.insert(END, '=============================================\nArticle_Name\t|\tQuantity\t | Rate [Of 1 Item]\n=============================================')
	textarea.config(state='disabled')

def exmsys():
	op = messagebox.askyesno("Exit", "Do you really want to exit?")
	if op > 0:
		sprz.destroy()

def svebil():
	x = generate()
	a = name.get()
	b = phone.get()
	c = paymentinfo.get()
	articles=textarea.get('1.0',END)
	sum_of_rate = sum(rate_of_items)
	if a=='' or b==0:
		messagebox.showerror('Detail Error','Customer Details Are Must!!!')
	elif c=='None':
		messagebox.showerror('Payment Error', 'Mode Of Payment Not Selected!')
	else:
		hehe = messagebox.askyesno('Save Bill', f'Do you want to save Bill with bill no. {x} of {a}')
		if hehe > 0:
			filer = open(f'Bills/bill {x} {a}.sprz', 'wt',encoding="utf8")
			filer.write(f"	  Welcome Krishna's Retail Shop\n\nBill Number:		{x}\nCustomer Name:		{a}\nPhone Number:		{b}\nPayment Done In:		{c}\n\n\n{articles}\n\n=============================================\nTotal Bill Amount :		      {sum_of_rate}\n\n=============================================")
			filer.close()
			with open(f"Bills/bill {x} {a}.sprz", "rb") as file:
				content = file.read()
				blah = Fernet(akey).encrypt(content)
			with open(f"Bills/bill {x} {a}.sprz", "wb") as wbf:
				wbf.write(blah)
			messagebox.showinfo('Bill Saved',f'Please review the Bill with number {x} of {a} in the Bills Folder.')
			clr()

def toggle_theme():
    if sv_ttk.get_theme() == "dark":
        sv_ttk.use_light_theme()
    else:
        sv_ttk.use_dark_theme()


#buttons
frame5 = ttk.LabelFrame(master_frame,text='Actions')
frame5.grid(row=1,column=0,padx=10,pady=5)
ttk.Button(frame5, text=' Add  ', command=lambda:mkebil(rate,quantity,item_name)).grid(row=0, column=0,pady=5,padx=5)
ttk.Button(frame5, text=' Save ',command=lambda:svebil()).grid(row=1, column=0,pady=5,padx=5)
ttk.Button(frame5, text=' Clear',command=lambda:clr()).grid(row=0, column=1,pady=5,padx=5)
ttk.Button(frame5, text=' Exit ',command=lambda:exmsys()).grid(row=1, column=1,pady=5,padx=5)
ttk.Button(frame5, text="Toggle Theme", command=toggle_theme).grid(row=2,column=0,padx=5,pady=5)
ttk.Button(frame5,text=' About ',command=lambda:messagebox.showinfo('About',f'Made by : TheHackerClown\nIssued : {date_issue}\nLicensed To : {user}')).grid(row=2,column=1,padx=5,pady=5)

#LOOPING
sv_ttk.set_theme('dark')
sprz.mainloop()
