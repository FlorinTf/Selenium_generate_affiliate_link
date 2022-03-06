import time
from tkinter import *
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.common.by import By
import webbrowser
from selenium.webdriver.chrome.options import Options
import os

user = os.environ.get("User")
password = os.environ.get("pass")
nume_client=[]
links=[]

root = Tk()
root.iconbitmap(r"Aliexpress.ico")
root.geometry("600x200")
root.title("Aliexpress Affiliate Link")
root.resizable(width=False,height=False)
bg = PhotoImage(file="bg.png")

def Add_nume():

    nume = input_nume.get()
    nume_client.append(nume)

def Link():
    link = input_link.get()
    links.append(link)
    root.quit()
my_canvas = Canvas(root, width=600, height=200)
my_canvas.pack(fill='both', expand=True,)
my_canvas.create_image(0,0, image=bg, anchor=NW)

nume_cumparator = Label(root, text= "Numele tau", font= ("Arial",15,"bold"), bg="#e52e04", fg="white")
nume_cumparator.place(x=230 , y=30)
input_nume = Entry(root,width= 20)
input_nume.place(x=350 , y=36)
enter_nume = Button(root, text= "Enter nume", font=("Arial", 12,"bold"),fg="#e52e04",command = Add_nume)
enter_nume.place(x=480 , y=32)

eticheta_link = Label(root, text= "Paste link:  Ctrl + V", font= ("Arial",15,"bold"),bg="#e52e04",fg="white")
eticheta_link.place(x=185 , y=165)
input_link = Entry(root,width= 70)
input_link.place(x=170 , y=131)
enter_link = Button(root, text= "Enter link", font= ("Arial",12,"bold"),command= Link,fg="#e52e04")
enter_link.place(x=400 , y=165)

root.mainloop()


website = "https://login.admitad.com/auth/realms/admitad/protocol/openid-connect/auth?client_id=monolith&redirect_uri=https%3A%2F%2Fstore.admitad.com%2Fen%2Fsso%2Flogin-complete%2F&response_type=code&scope=openid+email+profile&state=bad73024-d0fb-4764-afaf-240da652f803&ui_locales=en"
options = Options()
options.headless = True
s = service.Service("C:\SeleniumDrivers\chromedriver.exe")

driver = webdriver.Chrome(service = s, options=options)
PATH = "C:\SeleniumDrivers\chromedriver.exe"
driver.set_window_size(1920,1080)
driver.get(website)

link_final=[]


