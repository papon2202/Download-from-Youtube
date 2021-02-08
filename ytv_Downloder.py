from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube
Folder =""
#select folder
def location():
    global Folder
    Folder = filedialog.askdirectory()
    if(len(Folder)>1):
        path_error.config(text= Folder,bg ="green",fg ="white")
    else:
        path_error.config(text = "select the right folder",bg ="red")

#download
def download_video():
    choice = my_choice.get()
    url = yturl.get()
    if(len(url)>1):
        url_error.config(text="")
        yt=YouTube(url)
        if(choice==choices[0]):
            select = yt.streams.filter(progressive=True).first()
        elif(choice==choices[1]):
            select = yt.streams.filter(progressive=True).last()
        elif(choice==choices[2]):
            select = yt.streams.filter(only_audio=True).first()
        else:
            url_error.config(text="past the link again",bg = "yellow")
    select.download(Folder)
    url_error.config(text="Download Completed!!!!")

root = Tk()
root.title("YouTube Video Downloder")
root.geometry("350x450")
root.columnconfigure(0,weight =1)

hedding = Label(root,text = "Download From Youtube", font = ("Lucida Calligraphy",15,"bold"))
hedding.grid()

#url here
urlEntryVar = StringVar()
yturl = Entry(root,width = 40,textvariable = urlEntryVar)
yturl.grid()

#url error
url_error = Label(root,text = "Error Message",fg="red",font =("jost",10))
url_error.grid()
#save file
save_file = Label(root,text = "Save File", font = ("Lucida Calligraphy",17))
save_file.grid()

#select Folder Button
select_folder=Button(root,text="Select Folder",width =30, bg="red",command = location)
select_folder.grid()

#path error
path_error =Label(root,text="Folder Selection Error",fg="red", font =("jost",10))
path_error.grid()
#quality/type
quality = Label(root,text = "Select Quality",font = ("jost",15,"bold"))
quality.grid()
#choice
choices =["720","360","mp3"]
my_choice=ttk.Combobox(root,value = choices)
my_choice.grid()
#Download
download=Button(root,text ="Download",bg="red",width=10,command= download_video)
download.grid()


root.mainloop()