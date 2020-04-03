import tkinter as tk

if __name__ == "__main__":
    window = tk.Tk()
    window.title('TK窗口')
    window.geometry('400x400')
    
    lb1 = tk.Label(window, 
                    text='lable1',
                    bg='#aaeeee',
                    fg='red',
                    relief='raised'
                    )
    # lb1.pack()
    lb1.grid(column=2, row=0)
    
    lb2 = tk.Label(
        window,
        text='label2',
        fg='green',
        relief='groove'
    )
    # lb2.pack(side='right')
    lb2.grid(column=0, row=1)
    
    lb3 = tk.Label(
        window,
        text='label3',
        fg='blue',
        relief='raised'
    )
    # lb3.pack(fill='x')
    lb3.grid(column=1, columnspan=2, row=2, ipadx=30)
    
    window.mainloop()

