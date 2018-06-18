from tkinter import *
import ctypes
import os


def bg_red():
    print("red")
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "D:\\hallo.jpg", 0)


def bg_blue():
    print("BLUE")
    print("OS:", os.getcwd())


def bg_green():
    print("GREEEEEEN")


class Application(Frame):

    def create_widgets(self):
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "bottom"})

        self.RED["bg"] = "red"
        self.RED["command"] = bg_red
        self.RED.pack(side="left", anchor=W, fill=X, expand=YES)

        self.BLUE["bg"] = "blue"
        self.BLUE["command"] = bg_blue
        self.BLUE.pack(side="left", anchor=W, fill=X, expand=YES)

        self.GREEN["bg"] = "green"
        self.GREEN["command"] = bg_green
        self.GREEN.pack(side="left", anchor=W, fill=X, expand=YES)

    def __init__(self, master):
        print("__init__tkinter_test")

        fm = Frame.__init__(self, master)
        self.pack()
        self.RED = Button(fm)
        self.BLUE = Button(fm)
        self.GREEN = Button(fm)
        self.QUIT = Button(fm)
        self.create_widgets()


def start_form():
    root = Tk()
    root.minsize(350, 250)
    root.resizable(FALSE, FALSE)
    app = Application(master=root)
    app.master.title("Gaybi")
    app.mainloop()
    root.destroy()

