import tkinter as tk
import cv2
from PIL import Image, ImageTk

camera = cv2.VideoCapture(0)

def video_loop(*agrs):
    # print(camera)
    success, img = camera.read()
    if success:
        # print('abc')
        cv2Image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
        current_image = Image.fromarray(cv2Image)
        imgTk = ImageTk.PhotoImage(image=current_image)
        panel.imgTk = imgTk
        panel.config(image=imgTk)
        root.after(1,video_loop)

if __name__ == "__main__":
    # camera = cv2.VideoCapture()
    # fang[-1]
    root = tk.Tk()
    root.title('摄像头')
    root.geometry('800x600')
    # print('fang')
    panel = tk.Label(root)
    panel.place(relx = 0.3, rely = 0.3, relwidth = 0.5, relheight=0.5)
    root.config(cursor='arrow')

    video_loop()

    root.mainloop()

    camera.release()
    cv2.destroyAllWindows()