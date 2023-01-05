from modules import *
from modules.text_tab import text_tab

from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from os.path import basename

class dicto(Tk):
    def __init__(self, title="Dicto"):
        Tk.__init__(self)

        self._tab = []
        self._current_tab = 0
        self._number_of_tab = 1

        self._style = Style()
        self._style.theme_use('clam')

        self.title(title)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.create_menu_bar()
        
        self._tab_control = Notebook(self)
        self._tab.append(text_tab(self._tab_control))
        self._tab_control.add(self._tab[self._number_of_tab-1], text="Untitled")
        self._tab_control.grid(sticky="nsew", column=0, row=0)

        self._close_tab_button = Button(text="[×] Close current tab", command=self.close_current_tab)
        self._close_tab_button.grid(sticky="w")

        self._tab_control.bind("<<NotebookTabChanged>>", lambda func: self.tab_changed())

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
        if(self._number_of_tab > 1):
            del self._tab[self._current_tab]
            self._tab_control.forget(self._tab_control.select())
            self._number_of_tab -= 1

    def new_file(self):
        self._tab.append(text_tab(self._tab_control))
        self._tab_control.add(self._tab[self._number_of_tab], text="Untitled")
        self._tab_control.select(self._number_of_tab)

        self._number_of_tab += 1

    def open_file(self):
        path = askopenfilename()
        if len(path) != 0:
            try:
                file = open(path)
                content = file.read()
                file.close()

                self._tab.append(text_tab(self._tab_control))
                self._tab[self._number_of_tab].path = path

                self._tab_control.add(self._tab[self._number_of_tab], text=basename(path))
                self._tab_control.select(self._number_of_tab)
                self._tab[self._number_of_tab].textEdit.insert(1.0, content)
                
                self._number_of_tab += 1
            except UnicodeDecodeError:
                showerror(title="Error", message="That file can't be read")

    def save_file(self):
        if self._tab[self._current_tab].path == "":
            self._tab[self._current_tab].path = asksaveasfilename()

        if len(self._tab[self._current_tab].path) != 0:
            file = open(self._tab[self._current_tab].path, "w")
            file.write(self._tab[self._current_tab].textEdit.get(1.0, END))
            file.close()
            self._tab_control.tab(self._tab[self._current_tab], text=basename(self._tab[self._current_tab].path))
            
            
    def saveAs_file(self):
        path = asksaveasfilename()
        if len(path) != 0:
            file = open(path, "w")
            file.write(self._tab[self._current_tab].textEdit.get(1.0, END))
            file.close()

    def quit_window(self):
        if askyesno(title="Exit", message="Are you sure than you want to quit ?"):
            self.destroy()

    def about(self):
        showinfo(title="About", message="Dicto v1.0\nCreator : Fayred\nBuilt on 28 dec. 2022")

    def tab_changed(self):
        self._current_tab = self._tab_control.index(self._tab_control.select())
