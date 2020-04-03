import tkinter as tk

if __name__ == "__main__":
    window = tk.Tk()
    window.title('TK窗口')
    window.geometry('400x400')
    lb1 = tk.Label(window, text='lable1', bg='#aaeeee',
                   fg='red', relief='raised')
    lb1.pack()
    msg1 = tk.Message(window, 
        text='我的水平起始位置相对窗体 0.2，垂直起始位置为绝对位置 80 像素，我的高度是窗体高度的0.4，宽度是200像素',
        relief='raised')
    # msg1.pack()
    msg1.place(relx=0.2, y=100, relheight=0.5, width=200)
    window.mainloop()
