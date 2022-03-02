from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from tkinter.messagebox import *
import sys


class File():
    def newFile(self,event):
        self.filename = "Untitled"
        self.text.delete(0.0, END)

    def saveFile(self,event):
        try:
            t = self.text.get(0.0, END)
            f = open(self.filename, 'w')
            f.write(t)
            f.close()
        except:
            self.saveAs()

    def saveAs(self,event):
        f = asksaveasfile(mode='w', defaultextension='.txt')
        t = self.text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title="Oops!", message="Unable to save file...")

    def openFile(self,event):
        f = askopenfile(mode='r')

        self.filename = f.name
        t = f.read()
        self.text.delete(0.0, END)
        self.text.insert(0.0, t)

    def quit(self):
        entry = askyesno(title="Quit", message="Are you sure you want to quit?")
        if entry == True:
            self.root.destroy()

    def __init__(self, text, root):
        self.filename = None
        self.text = text
        self.root = root


def main(root, text, menubar):
    filemenu = Menu(menubar,tearoff=False)
    objFile = File(text, root)
    filemenu.add_command(label="New", command=objFile.newFile,accelerator="Ctrl+N")
    filemenu.add_command(label="Open", command=objFile.openFile,accelerator="Ctrl+O" )
    filemenu.add_command(label="Save", command=objFile.saveFile,accelerator="Ctrl+S" )
    filemenu.add_command(label="Save As...", command=objFile.saveAs,accelerator="Ctrl+Shift+S" )
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=objFile.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.bind_all("<Control-n>", objFile.newFile)
    root.bind_all("<Control-o>", objFile.openFile)
    root.bind_all("<Control-s>",objFile.saveFile)
    root.bind_all("<Control-s>", objFile.saveAs)
    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'main.py'")
