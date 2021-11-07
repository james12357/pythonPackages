import socket
from PIL import Image
import io
from PIL import ImageFile, ImageTk
import tkinter
import _thread

global i
root = tkinter.Tk()
ImageFile.LOAD_TRUNCATED_IMAGES = True
s = socket.socket()
s.bind((socket.gethostname(), 12366))
s.listen(5)
cv = tkinter.Canvas(root)
cv.pack(side=tkinter.TOP)


def b():
    global i
    while True:
        c, a = s.accept()
        co = c.recv(999999)
        bs = io.BytesIO(co)
        i = Image.open(bs)
        i = ImageTk.PhotoImage(i)
        t()


def t():
    root.after(100, t)
    cv.create_image(0, 0, image=i)


_thread.start_new_thread(b, ())
root.mainloop()

