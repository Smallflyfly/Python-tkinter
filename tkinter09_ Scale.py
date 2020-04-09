import tkinter as tk

def show(*agrs):
    s = '滑块的取值为' + str(var.get())
    lb.config(text=s)
    print(s)

if __name__ == "__main__":
    window = tk.Tk()
    window.title("滑块")
    window.geometry("400x400")
    
    var = tk.DoubleVar()
    scl = tk.Scale(window, orient='horizontal', length=200, from_=1.0, to=5.0, 
            label='请拖动滑块', tickinterval=1, resolution=0.05, variable=var)

    lb = tk.Label(window, text='')
    lb.pack()

    scl.bind('ButtonRelease-1', show)
    scl.pack()

    window.mainloop()