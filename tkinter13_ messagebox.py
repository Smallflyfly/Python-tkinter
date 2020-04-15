import tkinter as tk
import tkinter.messagebox

def xz(lb):
    answer = tkinter.messagebox.askokcancel('请选择', '请选择确定或者取消')
    if answer:
        lb.config(text='已确认')
    else:
        lb.config(text='已取消')

if __name__ == "__main__":
    window = tk.Tk()
    window.title('消息框')
    window.geometry('400x400')
    lb = tk.Label(window, text='')
    lb.pack()
    btn = tk.Button(window, text='弹出对话框', command=lambda:xz(lb))
    btn.pack()

    window.mainloop()

    