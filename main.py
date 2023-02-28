from subprocess import call
from tkinter import*
from tkinter import ttk
import pymysql
from tkinter import messagebox as box
from PIL import Image, ImageTk

db = pymysql.connect(host='localhost', user='root', password='zhn0946.', database="banksystem")
us_ma = db.cursor()


win_start= Tk()
win_start.geometry("440x370")
win_start.title("初始界面")

title_start = Label(win_start, text='请选择你的身份:', fg="black")
title_start.grid(row=1, column=1, padx=100)
Label.config(title_start, font=("Times New Roman", 30, "bold"))

def client():
    call(["python", "client.py"])

def manager():
    call(["python", "manager.py"])


def choice_user_manager():
    client_button = Button(win_start, text='我是客户', command=client, width=15, height=2, fg="black",
                           font=("halvatica", 20, "bold"))
    client_button.grid(row=3, column=1, padx=5, pady=40)

    manager_button = Button(win_start, text='我是管理员', command=manager, width=15, height=2, fg="black",
                            font=("halvatica", 20, "bold"))
    manager_button.grid(row=5, column=1, padx=5, pady=40)


choice_user_manager()
win_start.mainloop()