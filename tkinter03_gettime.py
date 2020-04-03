import tkinter as tk
import time


# def gettime():
#     timestr = time.strftime("%H:%M:%S")
#     time_label.configure(text=timestr)
#     window.after(1000, gettime)

def gettime():
    var.set(time.strftime('%Y-%m-%d %H:%M:%S'))
    window.after(1000, gettime)

window = tk.Tk()
window.title('时钟')
window.geometry('400x400')
var = tk.StringVar()
time_label = tk.Label(text='时钟', textvariable=var, fg='red', font=('黑体', 20))
# time_label.place(relx=0, rely=0.5)
time_label.pack()

if __name__ == "__main__":
    gettime()
    window.mainloop()
