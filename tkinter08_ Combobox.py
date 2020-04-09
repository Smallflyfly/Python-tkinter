import tkinter as tk
from tkinter import ttk

def cal(*args):
    # print(t1, t2)
    x = float(t1.get())
    y = float(t2.get())
    dic = {0:x+y, 1:x-y, 2:x*y, 3:x/y}
    c = dic[comb.current()]
    lab.config(text=str(c))

if __name__ == "__main__":
    window = tk.Tk()
    window.title("组合框 四则运算")
    window.geometry("400x400")

    t1 = tk.Entry(window)
    t1.place(relx=0.1, rely=0.1, relwidth=0.2, relheight=0.1)

    t2 = tk.Entry(window)
    t2.place(relx=0.5, rely=0.1, relwidth=0.2, relheight=0.1)

    lab = tk.Label(window, text='结果')
    lab.place(relx=0.5, rely=0.7, relwidth=0.6, relheight=0.2)

    var = tk.StringVar()
    comb = ttk.Combobox(window, textvariable=var, values=['加', '减', '乘', '除'])
    comb.place(relx=0.1, rely=0.5, relwidth=0.2)
    comb.bind('<<ComboboxSelected>>', cal)

    window.mainloop()