import tkinter as tk

def init(listbox):
    listbox.delete(0,'end')
    class_items = ['数学', '语文', '化学', '地里', '生物']
    for item in class_items:
        listbox.insert('end', item)

def add(entry, listbox):
    if entry.get() != '':
        if listbox.curselection() == ():
            listbox.insert('end', entry.get())
        else:
            listbox.insert(listbox.curselection(), entry.get())

def delete(listBox):
    if listBox.curselection() != ():
        listBox.delete(listBox.curselection())

def update(entry, listbox):
    if entry.get() != '' and listbox.curselection() != ():
        select = listbox.curselection()[0]
        listbox.delete((select,))
        listbox.insert((select,), entry.get())

def clear(listbox):
    listbox.delete(first=(0,), last=(listbox.size(),))

if __name__ == "__main__":
    window = tk.Tk()
    window.title('列表框')
    window.geometry('400x400')
    frame1 = tk.Frame(window, relief='raised')
    frame1.place(relx=0.0)

    frame2 = tk.Frame(window, relief='groove')
    frame2.place(relx=0.5)

    listBox1 = tk.Listbox(frame1)
    listBox1.pack()

    entry = tk.Entry(frame2)
    entry.pack()

    btn1 = tk.Button(frame2, text='初始化', command=lambda:init(listBox1))
    btn1.pack(fill='x')

    btn2 = tk.Button(frame2, text='插入', command=lambda:add(entry, listBox1))
    btn2.pack(fill='x')

    btn3 = tk.Button(frame2, text='删除', command=lambda:delete(listBox1))
    btn3.pack(fill='x')

    btn4 = tk.Button(frame2, text='更新', command=lambda:update(entry, listBox1))
    btn4.pack(fill='x')

    btn5 = tk.Button(frame2, text='清空', command=lambda:clear(listBox1))
    btn5.pack(fill='x')

    window.mainloop()