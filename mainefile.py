# from tkinter import *
# main=Tk()
# main.mainloop()

from tkinter import *
from tkinter.simpledialog import *
from tkinter.filedialog import *
from tkinter.messagebox import *

class edit():
    def popup(self,event):
        self.rightClick.post(event.x_root,event.y_root)
    def copy(self,*args):
        sel=self.text.selection_get()
        self.clipboard=sel
    def cut(self,*args):
     sel=self.text.selection_get()
     self.text.delete(SEL_LAST)