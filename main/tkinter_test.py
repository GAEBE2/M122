from tkinter import *
import ctypes
import os
from tkinter import filedialog





class Application(Frame):
    path = "Select an image to change the background"

    def create_widgets(self):
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "bottom"})

        self.PATH_TEXT.insert(INSERT, self.path)
        self.PATH_TEXT.pack()

        self.PATH_CHOOSER["text"] = "..."
        self.PATH_CHOOSER["command"] = self.select_path
        self.PATH_CHOOSER.pack(side="left", anchor=W, fill=X, expand=YES)

        self.CHANGE["text"] = "Change"
        self.CHANGE["state"] = "disabled"
        self.CHANGE["command"] = self.change_bg
        self.CHANGE.pack(side="left", anchor=W, fill=X, expand=YES)

    def change_bg(self):
        print("path: " + self.path)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, self.path, 3) #change bg

    def select_path(self):
        path = filedialog.askopenfilename(filetype=(("Images", ("*.jpg", "*.png", "*.jpeg")), ("All Files", "*.*")))

        if path == "":
            self.path = "Select an image to change the background"
            self.CHANGE["state"] = "disabled"
        else:
            self.path = path
            self.CHANGE["state"] = "normal"

        self.PATH_TEXT.delete('1.0', END)
        self.PATH_TEXT.insert(INSERT, self.path)


    def __init__(self, master):
        print("__init__tkinter_test")

        fm = Frame.__init__(self, master)
        self.pack()
        self.PATH_TEXT = Text(fm, height=1)
        self.PATH_CHOOSER = Button(fm)
        self.CHANGE = Button(fm)
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
