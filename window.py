from tkinter import *
from module1 import *
import threading
from data import data_game
from time import sleep


def datas(access):
    access.insert(0, "Kellega mängime? botVSbot-Botid playerVSbot-Robotiga")
    while True:
        m = data_game['kas']['mod']
        if m:
            v1=["Kivi","Käärid", "Paaber"]
            v2=["Kivi","Käärid", "Paaber"]
            r = m[-1]
            if r:
                robotvs(access)
            else:
                botvsbot(v1,v2, access)
        sleep(.5)

def erigid(bcolor,fcolor):
    menuska3=Toplevel()
    menuska3.grab_set()
    menuska3.geometry("600x600")
    menuska3.configure(bg="#404040")
    menuska3.focus_force()
    lists = Listbox(menuska3, width=50, height=50)
    lists.pack(side=RIGHT)
    #select rigid



def kas():
    def game_kas(bcolor,fcolor):
        menuska2=Toplevel()
        menuska2.grab_set()
        menuska2.geometry("600x600")
        menuska2.configure(bg="#404040")
        menuska2.focus_force()
        lists = Listbox(menuska2, width=50, height=50)
        lists.pack(side=RIGHT)
        # select game
        btn8=Button(menuska2, width=20, height=2, text='botVSbot',
            fg=bcolor,
            bg=fcolor,
            command=lambda *args: data_game['kas']['mod'].append(0),
            border=0,
            activeforeground=fcolor,
            activebackground=bcolor)
        btn8.pack(side=TOP)
        btn9=Button(menuska2, width=20, height=2, text='playerVSbot',
            fg=bcolor,
            bg=fcolor,
            command=lambda *args: data_game['kas']['mod'].append(1),
            border=0,
            activeforeground=fcolor,
            activebackground=bcolor)
        btn9.pack(side=TOP)
        # game
        btn5=Button(menuska2, width=7, height=2, text='1',
            fg=bcolor,
            bg=fcolor,
            command=lambda *args: data_game['kas']['user'].append(1),
            border=0,
            activeforeground=fcolor,
            activebackground=bcolor)
        btn5.pack(side=LEFT)
        btn6=Button(menuska2, width=7, height=2, text='2',
            fg=bcolor,
            bg=fcolor,
            command=lambda *args: data_game['kas']['user'].append(2),
            border=0,
            activeforeground=fcolor,
            activebackground=bcolor)
        btn6.pack(side=LEFT)
        btn7=Button(menuska2, width=7, height=2, text='3',
            fg=bcolor,
            bg=fcolor,
            command=lambda *args: data_game['kas']['user'].append(3),
            border=0,
            activeforeground=fcolor,
            activebackground=bcolor)
        btn7.pack(side=LEFT)

        return lists

    access = game_kas('#C3E88D', '#2196F3')
    threading.Thread(target=lambda: datas(access)).start()




def menuska(bcolor,fcolor):
    menuska=Toplevel()
    menuska.grab_set()
    menuska.geometry("300x600")
    menuska.configure(bg="#141414")

    btn1=Button(menuska, width=42, height=2, text="K ä ä r i d, K i v i, P a p e r",
                fg=bcolor,
                bg=fcolor,
                border=0,
                command=kas,
                activeforeground=fcolor,
                activebackground=bcolor).grid(row=0, column=0)

    btn2=Button(menuska, width=42, height=2, text='E U R O O P A   R I I G I D',
                fg=bcolor,
                bg=fcolor,
                border=0,
                command=erigid,
                activeforeground=fcolor,
                activebackground=bcolor).grid(row=1, column=0)

    btn3=Button(menuska, width=42, height=2, text='b',
                fg=bcolor,
                bg=fcolor,
                command=lambda: 'test',
                border=0,
                activeforeground=fcolor,
                activebackground=bcolor).grid(row=2, column=0)

    btn4=Button(menuska, width=42, height=2, text='c',
                fg=bcolor,
                bg=fcolor,
                border=0,
                command=lambda: 'test',
                activeforeground=fcolor,
                activebackground=bcolor).grid(row=3, column=0)


def btn_clicked():
    login = entry0.get()
    password = entry1.get()

    user = f'{login},{password}'

    with open('db.txt') as file:
        db = file.readlines()

    if user in db:
        menuska("#ffcc66", "#141414")
        window.withdraw()
        print('good')
    else:
        print('bad')

window = Tk()

window.geometry("1440x1024")
window.configure(bg="#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    826.0, 441.5,
    image=background_img)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    275.5, 135.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#fffafa",
    highlightthickness = 0)

entry0.place(
    x = 99.0, y = 89,
    width = 353.0,
    height = 90)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    275.5, 298.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#fffafa",
    highlightthickness = 0)

entry1.place(
    x = 99.0, y = 252,
    width = 353.0,
    height = 90)


img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 189, y = 385,
    width = 174,
    height = 96)


window.resizable(False, False)
window.mainloop()
