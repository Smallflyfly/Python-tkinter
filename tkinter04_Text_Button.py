import tkinter as tk
import time
import datetime

def gettime(window, txt):
    s = str(datetime.datetime.now()) + '\n'
    txt.insert('end',s)
    window.after(1000, lambda:gettime(window, txt))

def run(input_x, input_y, txt):
    x = float(input_x.get())
    y = float(input_y.get())
    s = '%0.2f + %0.2f = %0.2f\n' % (x, y, x+y)
    txt.insert('end', s)
    input_x.delete(0,'end')
    input_y.delete(0,'end')

if __name__ == "__main__":
    window = tk.Tk()
    window.title('简单加法器')
    window.geometry('400x400')
    lb1 = tk.Label(window, text="请输入数字")
    lb1.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
    # 输入框
    input1 = tk.Entry(window)
    input1.place(relx=0.1, rely=0.2, relwidth=0.2, relheight=0.1)
    input2 = tk.Entry(window)
    input2.place(relx=0.4, rely=0.2, relwidth=0.2, relheight=0.1)

    lb2 = tk.Label(window, text="+")
    lb2.place(relx = 0.3, rely=0.2, relwidth=0.1, relheight=0.1)
    #输出文本
    txt = tk.Text(window)
    txt.place(rely=0.5, relheight=0.2)

    #按钮
    btn1 = tk.Button(window, text='加法', command=lambda:run(input1, input2, txt))
    btn1.place(relx=0.7, rely=0.2, relwidth=0.2, relheight=0.1)

    tk.mainloop()