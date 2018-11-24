from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog
from tkinter.font import Font

class text_editor():

   current_open_file="no_file"

   #this command is for File_menu

   def new_file(self,events=""):
       self.text_area.delete(1.0 , END)
       self.current_open_file="no_file"

   def open_file(self,events=""):
       open_result=filedialog.askopenfile(initialdir="/" , title="select file to open" , filetypes=(("text files", "*.txt"), ("all files", "*.*")))
       if (open_result!=None):
           self.text_area.delete(1.0,END)
           for line in open_result:
               self.text_area.insert(END,line)
       self.current_open_file = open_result.name
       open_result.close()

   def save_as_file(self):
       f=filedialog.asksaveasfile(mode="w" ,defaultextension=".txt")
       if f is None:
           return
       text2save=self.text_area.get(1.0,END)
       self.current_open_file = f.name
       f.write(text2save)
       f.close()

   def save_file(self,events=""):
       if self.current_open_file=="no_file":
           self.save_as_file()
       else:
           f=open(self.current_open_file ,"w+")
           f.write(self.text_area.get(1.0,END))
           f.close()

   def exit_file(self):
       quit=messagebox.askyesno("Quit", "Are you want to quit?")
       root.destroy()

   # this command is for Edit_menu

   def copy_text(self):
       self.text_area.clipboard_clear()
       self.text_area.clipboard_append(self.text_area.selection_get())

   def cut_text(self):
       self.copy_text()
       self.text_area.delete("sel.first", "sel.last")

   def paste_text(self):
       self.text_area.insert(INSERT,self.text_area.clipboard_get())

   # this command is for Format_menu

   def word_wrap(self):
       self.text_area=Text(root,wrap=WORD)

   def font(self):
       self.font = Font(family="Times New Roman", size=40, weight="bold", slant="italic")
       self.text_area=Text(root,font=self.font)


   # this command is for View_menu

   def status_bar_text(self):
       print("sameer")

   # this command is for Help_menu

   def about_text_editior(self):
       self.Label=messagebox.showinfo("About_text_editior", "A Python Alternative to Notepad")

   def search_text(self):
       self.findString=simpledialog.askstring("Find", "Enter_Text")
       found_text=self.text_area.get('1.0', END)

       occurences=found_text.upper().count(self.findString.upper())

       if found_text.upper().count(self.findString.upper())>0 :
               answer=messagebox.showinfo("Result", self.findString +"has multiple occurence" +str(occurences))
       else:
           answer = messagebox.showinfo("Result", " Sorry Match not found")



   def __init__(self,master):
        self.master=master
        master.title("texteditior")
        self.text_area=Text(wrap=WORD,undo=True)
        self.text_area.pack(fill=BOTH, expand=1)
        self.main_menu=Menu()
        self.master.config(menu=self.main_menu)

        #creating file_menu
        self.file_menu=Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        master.bind('<Control-n>',self.new_file)
        self.file_menu.add_command(label="New               Ctrl+N", command=self.new_file)
        master.bind('<Control-o>', self.open_file)
        self.file_menu.add_command(label="Open...          Ctrl+O", command=self.open_file)
        self.file_menu.add_separator()
        master.bind('<Control-s>', self.save_file)
        self.file_menu.add_command(label="Save               Ctrl+S", command=self.save_file)
        self.file_menu.add_command(label="Save_As ", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit ", command=self.exit_file)

        # creating edit_menu
        self.edit_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo        Ctrl+Z", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copy        Ctrl+C", command=self.copy_text)
        self.edit_menu.add_command(label="Cut           Ctrl+X", command=self.cut_text)
        self.edit_menu.add_command(label="Paste        Ctrl+V", command=self.paste_text)

       # creating format_menu
        self.format_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Format", menu=self.format_menu)
        self.format_menu.add_command(label="Word Wrap", command=self.word_wrap)
        self.format_menu.add_command(label="Font...", command=self.font)

        # creating view_menu
        self.view_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Status_Bar", command=self.status_bar_text)

        # creating help_menu
        self.help_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Help", menu=self.help_menu)
        self.help_menu.add_command(label="View Help", command=self.search_text)
        self.help_menu.add_separator()
        self.help_menu.add_command(label="About Texteditior", command=self.about_text_editior)

root=Tk()
te=text_editor(root)



root.geometry("400x400")
root.mainloop()
