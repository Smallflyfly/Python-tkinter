import tkinter as tk
import tkinter.simpledialog

def xz(lb, *args):
    s = tk.simpledialog.askstring('请输入', '请输入一串文字')
    lb.config(text=s)

if __name__ == "__main__":
    window = tk.Tk()
    window.title('输入框')
    window.geometry('400x400')

    lb = tk.Label(window, text='输入框')
    lb.pack()

    btn = tk.Button(window, text='弹出输入对话框', command=lambda:xz(lb))
    btn.pack()

    window.mainloop()

