from password_gen import PasswordGen
from tkinter import *
from tkinter import ttk
import tkinter


file = open('presets.txt', 'w+')
file.close()
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


def delete_preset(choice, menu):
    file = open('presets.txt', 'r+')
    contents = file.read()
    file.close()
    if str(dropdown_var.get()) in contents:
        file = open('presets.txt', 'r+')
        lines = file.readlines()
        for indx, line in enumerate(lines):
            if str(dropdown_var.get()) in line:
                lines.pop(indx)
                file.close()
                dropdown_var.set(choice[indx - 1])
                choice.pop(indx)
                break
        file = open('presets.txt', 'w')
        file.writelines(lines)
        file.close()
        menu.configure(values=choice)


def create_window():
    window = tkinter.Toplevel(root)
    pop_up_frame = ttk.Frame(window, padding='25 25 25 25')
    pop_up_frame.grid()
    pop_up_frame.columnconfigure(0, weight=1)
    pop_up_frame.rowconfigure(0, weight=1)
    rename_entry = ttk.Entry(pop_up_frame, width=20, textvariable=rename)
    rename_entry.grid(column=1, row=1, sticky=(W, E))
    ttk.Button(pop_up_frame, text='Ok', command=lambda: rename_preset(window)).grid(column=2, row=1, sticky=W)
    ttk.Label(pop_up_frame, text='Enter new name').grid(column=0, row=1, sticky=W)
    window.minsize(width=200, height=100)
    for child in pop_up_frame.winfo_children():
        child.grid_configure(padx=5, pady=5)
    center_window(window)


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
    if str(dropdown_var.get()) in contents:
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
            break
    line_list_digit = ['', '', '']
    for indx, string in enumerate(line_list):
        for c in string:
            if c.isdigit():
                line_list_digit[indx] += c
    length.set(line_list_digit[1])
    dist.set(line_list_digit[2])
    file.close()


def add_preset(choice, menu):
    choice.append('Preset ' + str(len(choice) + 1))
    menu.configure(values=choice)
    dropdown_var.set(choice[len(choice) - 1])
    file = open('presets.txt', 'a+')
    file.write("%s,%s,%s\n" % (str(dropdown_var.get()), str(length.get()), str(dist.get())))


def create_choice():
    file = open('presets.txt', 'r+')
    lines = file.readlines()
    choices = []
    for line in lines:
        temp = line.split(',')
        choices.append(temp[0])
    if not choices:
        dropdown_var.set('')
    else:
        dropdown_var.set(choices[0])
    return choices


def rename_preset(window):
    window.destroy()
    file = open('presets.txt', 'r+')
    lines = file.readlines()
    file.close()
    file = open('presets.txt', 'r+')
    contents = file.read()
    file.close()
    if str(rename.get()) not in contents:
        for indx, line in enumerate(lines):
            if str(dropdown_var.get()) in line:
                lines[indx] = "%s,%s,%s\n" % (str(rename.get()), str(length.get()), str(dist.get()))
                file = open('presets.txt', 'w')
                file.writelines(lines)
                file.close()
                for indx, val in enumerate(choice):
                    if val == str(dropdown_var.get()):
                        choice[indx] = str(rename.get())
                pop_menu.configure(values=choice)
                dropdown_var.set(str(rename.get()))
                break


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
rename = StringVar()

length_entry = ttk.Entry(mainframe, width=7, textvariable=length)
length_entry.grid(column=2, row=2, sticky=(W, E))

dist_entry = ttk.Entry(mainframe, width=25, textvariable=dist)
dist_entry.grid(column=2, row=3, sticky=(W, E))

password_entry = ttk.Entry(mainframe, width=25, textvariable=password)
password_entry.grid(column=2, row=4, sticky=(W, E))
password_entry.config(state='readonly')

ttk.Button(mainframe, text='Generate', command=create_object).grid(column=4, row=5, sticky=W)
ttk.Button(mainframe, text='Copy to clipboard', command=copy_clipboard).grid(column=2, row=5, sticky=W)
ttk.Button(mainframe, text='Save preset', command=save_preset).grid(column=2, row=1, sticky=W)
ttk.Button(mainframe, text='Load preset', command=load_preset).grid(column=2, row=1, sticky=E)
ttk.Button(mainframe, text='Add preset', command=lambda: add_preset(choice, pop_menu)).grid(column=2, row=0, sticky=W)
ttk.Button(mainframe, text='Rename', command=create_window).grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text='Delete preset', command=lambda: delete_preset(choice, pop_menu)).grid(column=2, row=0, sticky=E)

ttk.Label(mainframe, text='Length').grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text='Password').grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text='Dist').grid(column=1, row=3, sticky=W)

rb1 = ttk.Radiobutton(mainframe, text='Symbols', variable=symb_bool, value=True)
rb1.grid(column=4, row=2, sticky=W)
rb1.invoke()
ttk.Radiobutton(mainframe, text='No symbols', variable=symb_bool, value=False).grid(column=4, row=3, sticky=W)

ttk.Checkbutton(mainframe, text='Auto-mark', variable=mark_bool).grid(column=4, row=4, sticky=W)

choice = create_choice()
pop_menu = ttk.Combobox(mainframe, state='readonly', takefocus=False, textvariable=dropdown_var, values=choice)
pop_menu.grid(column=1, row=0, sticky=(W, E))
style = ttk.Style()
style.configure('TCheckbutton', focuscolor=root.cget("background"))
style.configure('TCheckbutton', activebackground=root.cget("background"))
style.configure('TCheckbutton', background=root.cget("background"))

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

length_entry.focus()
center_window(root)
root.mainloop()

