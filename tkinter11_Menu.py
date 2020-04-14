import tkinter as tk

def new():
    pass

def open():
    pass

def save():
    pass

def popupmenu(event, *args):
    mainmenu.post(event.x_root, event.y_root)


if __name__ == "__main__":
    window = tk.Tk()
    window.title('菜单')
    window.geometry('400x400')
    lb = tk.Label(window, text='显示信息', font=('黑体',32,'bold'))
    lb.place(relx=0.2, rely=0.2)

    mainmenu = tk.Menu(window)
    menuFile = tk.Menu(mainmenu)
    mainmenu.add_cascade(label='文件', menu=menuFile)
    menuFile.add_command(label='新建', command=new)
    menuFile.add_command(label='打开', command=open)
    menuFile.add_command(label='保存', command=save)
    menuFile.add_separator()
    menuFile.add_command(label='退出', command=window.destroy)

    window.config(menu=mainmenu)
    window.bind('Button-3', popupmenu)

    window.mainloop()