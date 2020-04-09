import tkinter as tk

def run(checkVal1, checkVal2, checkVal3, checkVal4, lb):
    if checkVal1.get() == 0 and checkVal2.get() == 0 \
            and checkVal3.get() == 0 and checkVal4.get() == 0:
        s = '你没有选择任何项目'
    else:
        s1 = '足球' if checkVal1.get() == 1 else ''
        s2 = '篮球' if checkVal2.get() == 1 else ''
        s3 = '台球' if checkVal3.get() == 1 else ''
        s4 = '地球' if checkVal4.get() == 1 else ''
        s = '%s %s %s %s' % (s1, s2, s3, s4)
        lb.config(text=s)
    

if __name__ == "__main__":
    window = tk.Tk()
    window.title("复选框")
    window.geometry('200x200')
    lb1 = tk.Label(window, text='请选择你的爱好项目')
    lb1.pack()

    checkVal1 = tk.IntVar()
    checkVal2 = tk.IntVar()
    checkVal3 = tk.IntVar()
    checkVal4 = tk.IntVar()

    ch1 = tk.Checkbutton(window, text='足球', variable=checkVal1, onvalue=1, offvalue=0)
    ch1.pack()
    ch2 = tk.Checkbutton(window, text='篮球', variable=checkVal2, onvalue=1, offvalue=0)
    ch2.pack()
    ch3 = tk.Checkbutton(window, text='台球', variable=checkVal3, onvalue=1, offvalue=0)
    ch3.pack()
    ch4 = tk.Checkbutton(window, text='地球', variable=checkVal4, onvalue=1, offvalue=0)
    ch4.pack()

    lb2 = tk.Label(window, text='')
    lb2.pack()

    btn = tk.Button(window, text='OK', command=lambda:run(checkVal1, checkVal2, checkVal3, checkVal4, lb2))
    btn.pack()

    window.mainloop()