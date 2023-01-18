from modules import *

class text_tab(Frame):
    def __init__(self, root):
        Frame.__init__(self, master=root)
        self.path = ""
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.textEdit = Text(self, font=("Courier", 14))
        self.textEdit.grid(sticky="nsew", row=0, column=0, padx=5, pady=5)  