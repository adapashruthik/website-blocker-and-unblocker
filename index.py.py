from tkinter import *
import datetime
#window creating
root=Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("website blocker and unblocker")
#heading
Label(root,text='mini project website blocker and unblocker',font='arial 16 bold').pack()
#laptop path saved location of data 
host_path='C:\\Windows\\System32\\drivers\\etc\\hosts'
#laptop server id
ip_address='127.0.0.1'
#date and time label
now=datetime.datetime.now()
Label(root,text='Date and Time:{}-{}-{},{}:{}:{}'.format(now.year,now.month,now.day,now.hour,now.minute,now.second),font='arial 10 bold').place(x=5,y=30)
#website input field
Label(root,text='enter a website name:',font='arial 10 bold').place(x=5,y=60)
Websites=Text(root,font='arial 10',height='2',width='40',wrap=WORD,padx=5,pady=5)
Websites.place(x=180,y=60)
#main blocker code
def Blocker():
    website_lists=Websites.get(1.0,END)
    Website=list(website_lists.split(","))
    with open(host_path,'r+')as host_file:
        file_content=host_file.read()
        for website in Website:
            if website in file_content:
                Label(root,text='you blocked already',font='arial 12 bold').place(x=200,y=200)
                pass
            else:
                host_file.write(ip_address+" "+website+'\n')
                Label(root,text="blocked website at {}-{}-{},{}:{}:{}".format(now.year,now.month,now.day,now.hour,now.minute,now.second),font='arial 12 bold').place(x=200,y=200)
#unblocker code 
def Unblock():
    website_lists=Websites.get(1.0,END)
    Website=list(website_lists.split(","))
    with open(host_path,'r+')as host_file:
        file_content=host_file.readlines()
        host_file.seek(0)
        for line in file_content:
            if not any(site in line for site in Website): 
                host_file.write(line) 
                Label(root,text="UnBlocked website at {}-{}-{},{}:{}:{}".format(now.year,now.month,now.day,now.hour,now.minute,now.second),font='arial 12 bold').place(x=200,y =230)
        host_file.truncate()
#block button 
block_btn=Button(root,text='block',font='arial 13 bold',command=Blocker,height=2,width=10,bg='white',activebackground='black')
#position on innterface
block_btn.place(x=200,y=140) 
#unblock button
unblock_button=Button(root,text='unblock',font='arial 13 bold',command=Unblock,height=2,width=10,bg='light green',activebackground='black')
#position on innterface
unblock_button.place(x=350,y=140)
root.mainloop()
