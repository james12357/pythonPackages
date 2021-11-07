import tkinter
import _thread


def mn():
    while True:
        tkinter.Tk().mainloop()


def run():
    while True:
        _thread.start_new_thread(mn, ())


while True:
    run()
