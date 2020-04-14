import tkinter as tk

def newWind(window, *args):
    winNew = tk.Toplevel(window)
    winNew.geometry('200x200')
    winNew.title('新窗口')
    lb = tk.Label(winNew, text='这是新窗口')
    lb.pack()
    btn = tk.Button(winNew, text='关闭', command=winNew.destroy)
    btn.place(relx=0.5, rely=0.5)

if __name__ == "__main__":
    window = tk.Tk()
    window.title('菜单')
    window.geometry('400x400')
    lb = tk.Label(window, text='主窗体', font=('黑体', 32, 'bold'))
    lb.place(relx=0.2, rely=0.2)
    mainmenu = tk.Menu(window)
    menuFile = tk.Menu(mainmenu)
    mainmenu.add_cascade(label='菜单',menu=menuFile)
    menuFile.add_command(label='新窗体',command=lambda:newWind(window))
    menuFile.add_separator()
    menuFile.add_command(label='退出', command=window.destroy)

    window.config(menu=mainmenu)

    window.mainloop()