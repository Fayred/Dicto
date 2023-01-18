from modules import *
from modules.text_tab import text_tab

from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from os.path import basename

class dicto(Tk):
    def __init__(self, title="Dicto"):
        Tk.__init__(self)
        self.tab = []
        self.current_tab = 0
        self.number_of_tab = 1

        self.style = Style()
        self.style.theme_use('clam')

        self.title(title)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_menu_bar()
        
        self.tab_control = Notebook(self)
        self.tab.append(text_tab(self.tab_control))
        self.tab_control.add(self.tab[self.number_of_tab-1], text="Untitled")
        self.tab_control.grid(sticky="nsew", column=0, row=0)

        self.close_tab_button = Button(text="[×] Close current tab", command=self.close_current_tab)
        self.close_tab_button.grid(sticky="w")

        self.tab_control.bind("<<NotebookTabChanged>>", lambda func: self.tab_changed())

    def create_menu_bar(self):
        menu_bar = Menu(self)
        self.config(menu=menu_bar)

        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="New", command=self.new_file)
        menu_file.add_command(label="Open", command=self.open_file)
        menu_file.add_command(label="Save", command=self.save_file)
        menu_file.add_command(label="Save as", command=self.saveAs_file)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.quit_window)
        menu_bar.add_cascade(label="File", menu=menu_file)

        menu_help = Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="About", command=self.about)
        menu_bar.add_cascade(label="Help", menu=menu_help)

    def close_current_tab(self):
        if(self.number_of_tab > 1):
            del self.tab[self.current_tab]
            self.tab_control.forget(self.tab_control.select())
            self.number_of_tab -= 1

    def new_file(self):
        self.tab.append(text_tab(self.tab_control))
        self.tab_control.add(self.tab[self.number_of_tab], text="Untitled")
        self.tab_control.select(self.number_of_tab)

        self.number_of_tab += 1

    def open_file(self):
        path = askopenfilename()
        if len(path) != 0:
            try:
                file = open(path)
                content = file.read()
                file.close()

                self.tab.append(text_tab(self.tab_control))
                self.tab[self.number_of_tab].path = path

                self.tab_control.add(self.tab[self.number_of_tab], text=basename(path))
                self.tab_control.select(self.number_of_tab)
                self.tab[self.number_of_tab].textEdit.insert(1.0, content)
                
                self.number_of_tab += 1
            except UnicodeDecodeError:
                showerror(title="Error", message="That file can't be read")

    def save_file(self):
        if self.tab[self.current_tab].path == "":
            self.tab[self.current_tab].path = asksaveasfilename()

        if len(self.tab[self.current_tab].path) != 0:
            file = open(self.tab[self.current_tab].path, "w")
            file.write(self.tab[self.current_tab].textEdit.get(1.0, END))
            file.close()
            self.tab_control.tab(self.tab[self.current_tab], text=basename(self.tab[self.current_tab].path))
            
            
    def saveAs_file(self):
        path = asksaveasfilename()
        if len(path) != 0:
            file = open(path, "w")
            file.write(self.tab[self.current_tab].textEdit.get(1.0, END))
            file.close()

    def quit_window(self):
        if askyesno(title="Exit", message="Are you sure than you want to quit ?"):
            self.destroy()

    def about(self):
        showinfo(title="About", message="Dicto v1.0\nCreator : Fayred\nBuilt on 28 dec. 2022")

    def tab_changed(self):
        self.current_tab = self.tab_control.index(self.tab_control.select())