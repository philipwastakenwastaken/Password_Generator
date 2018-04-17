from password_gen import PasswordGen
from tkinter import *
from tkinter import ttk


root = Tk()
root.title('Password Generator')
root.minsize(width=350, height=100)


def center_window(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def create_object():
    if length.get() != '' and length.get().isdigit() and dist.get() != '' and dist.get().isdigit():
        pass_gen = PasswordGen(int(length.get()), int(dist.get()))
        if bool(symb_bool.get()):
            password.set(pass_gen.gen_pass_symbols())
        else:
            password.set(pass_gen.gen_pass_no_symbols())
        if bool(mark_bool.get()):
            password_entry.selection_range(0, END)
            password_entry.focus()


def copy_clipboard():
    root.clipboard_clear()
    root.clipboard_append(str(password.get()))
    root.update()


def save_preset():
    file = open('presets.txt', 'r+')
    contents = file.read()
    if str(dropdown_var.get()) not in contents:
        file = open('presets.txt', 'a+')
        file.write("%s,%s,%s\n" % (str(dropdown_var.get()), str(length.get()), str(dist.get())))
    else:
        file = open('presets.txt', 'r+')
        lines = file.readlines()
        for indx, line in enumerate(lines):
            if str(dropdown_var.get()) in line:
                lines[indx] = "%s,%s,%s\n" % (str(dropdown_var.get()), str(length.get()), str(dist.get()))
                break
        file = open('presets.txt', 'w')
        file.writelines(lines)
        file.close()


def load_preset():
    file = open('presets.txt', 'r+')
    lines = file.readlines()
    line_list = []
    for indx, line in enumerate(lines):
        if str(dropdown_var.get()) in line:
            line_list = line.split(',')


mainframe = ttk.Frame(root, padding='25 25 25 25')
mainframe.grid()
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

symb_bool = BooleanVar()
mark_bool = BooleanVar()
length = StringVar()
password = StringVar()
dropdown_var = StringVar()
dist = StringVar()

choice = ['Preset 1', 'Preset 2', 'Preset 3']
pop_menu = ttk.Combobox(mainframe, textvariable=dropdown_var, values=choice)
pop_menu.grid(column=1, row=0, sticky=(W, E))
dropdown_var.set('Preset 1')
length_entry = ttk.Entry(mainframe, width=7, textvariable=length)
length_entry.grid(column=2, row=1, sticky=(W, E))

dist_entry = ttk.Entry(mainframe, width=25, textvariable=dist)
dist_entry.grid(column=2, row=2, sticky=(W, E))

password_entry = ttk.Entry(mainframe, width=25, textvariable=password)
password_entry.grid(column=2, row=3, sticky=(W, E))
password_entry.config(state='readonly')

ttk.Button(mainframe, text='Generate', command=create_object).grid(column=4, row=4, sticky=W)
ttk.Button(mainframe, text='Copy to clipboard', command=copy_clipboard).grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, text='Save preset', command=save_preset).grid(column=2, row=0, sticky=W)
ttk.Button(mainframe, text='Load preset', command=load_preset).grid(column=2, row=0, sticky=E)

ttk.Label(mainframe, text='Length').grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text='Password').grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text='Dist').grid(column=1, row=2, sticky=W)

rb1 = ttk.Radiobutton(mainframe, text='Symbols', variable=symb_bool, value=True)
rb1.grid(column=4, row=1, sticky=W)
rb1.invoke()
ttk.Radiobutton(mainframe, text='No symbols', variable=symb_bool, value=False).grid(column=4, row=2, sticky=W)

ttk.Checkbutton(mainframe, text='Auto-mark', variable=mark_bool).grid(column=4, row=3, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

length_entry.focus()
center_window(root)
file = open('presets.txt', 'a+')
file.close()
root.mainloop()

