import tkinter as tk


def mychoose(var, lb):
    dit = {0: '甲', 1: '乙', 2: '丙'}
    s = 'you choose %s\n' % (dit[var.get()])
    lb.config(text=s)


if __name__ == "__main__":
    window = tk.Tk()
    window.title('单选按钮')
    window.geometry('400x400')
    lb = tk.Label(window)
    lb.pack()

    var = tk.IntVar()
    rad1 = tk.Radiobutton(window, text='甲', variable=var,
                          value=0, command=lambda: mychoose(var, lb))
    rad1.pack()
    rad2 = tk.Radiobutton(window, text='乙', variable=var,
                          value=1, command=lambda: mychoose(var, lb))
    rad2.pack()
    rad3 = tk.Radiobutton(window, text='丙', variable=var,
                          value=2, command=lambda: mychoose(var, lb))
    rad3.pack()

    window.mainloop()
