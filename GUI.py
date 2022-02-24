from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from fastdupes import main
class Gui:
    def __init__(self,root,path):
        self.path=path
        self.root=root
        self.buttonDir=ttk.Button(root,command=self.chooseDirectory,text="Choose Directory")
        self.labelDir=ttk.Label(root,text="choose Directory")
        self.labelalarm=ttk.Label(root)
        self.buttonDel=ttk.Button(root,command=self.deleteDirectory,text="<<<DelDup>>>")
        self.labelDel=ttk.Label(root,text="Delete duplicate!")
        self.labelDir.grid(row=0,column=0)
        self.buttonDir.grid(row=0,column=1)
        self.labelDel.grid(row=1,column=0)
        self.buttonDel.grid(row=1,column=1)
        self.buttonDel.state(['disabled'])
        self.labelalarm.grid(row=2,column=0,columnspan=2)
        self.labelalarm.config(text="")

    def chooseDirectory(self):
        directoryname = filedialog.askdirectory()
        if directoryname:
            self.path = directoryname
            self.root.title(" - ".join(["Duplicate remove",self.path]))
            self.buttonDel.state(['!disabled'])
            self.labelalarm.config(text="")
    def deleteDirectory(self):
        main(self.path)
        self.labelalarm.config(text="All duplicate removed!!")



