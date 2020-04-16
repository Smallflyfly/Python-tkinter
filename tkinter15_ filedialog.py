import tkinter as tk
import tkinter.filedialog

def uploadFile(*agrs):
    filename = tk.filedialog.askopenfile().name
    print(filename)
    if filename != '':
        lb.config(text=filename)
    else:
        lb.config(text='未选择任何文件')

if __name__ == "__main__":
    window = tk.Tk()
    window.title('文件导入')
    window.geometry('400x400')

    lb = tk.Label(window, text='文件')
    lb.pack()

    btn = tk.Button(window, text='选择文件', command=uploadFile)
    btn.pack()

    window.mainloop()