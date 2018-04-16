import random
from tkinter import *
from tkinter import ttk


class PasswordGen:

    def __init__(self, len, dist):
        self.len = len
        self.dist = dist

    # generates password from ASCII codes [33;126]
    def gen_pass_simp(self):
        pass_string = ''
        for i in range(self.len):
            pass_string += chr(random.randint(33, 126))
        return pass_string

    def int_to_ascii(self, pass_list):
        for index, val in enumerate(pass_list):
            pass_list[index] = chr(val)

    def gen_pass(self, symbol_range_list, word_range_list):
        pass_list = self.create_pass_list(symbol_range_list, word_range_list)
        self.int_to_ascii(pass_list)
        random.shuffle(pass_list)
        return ''.join(str(x) for x in pass_list)

    def gen_pass_symbols(self):
        symbol_range_list = list(range(33, 65)) + list(range(91, 97)) + list(range(123, 127))
        word_range_list = list(range(65, 81)) + list(range(97, 123))
        return self.gen_pass(symbol_range_list, word_range_list)

    def gen_pass_no_symbols(self):
        word_range_list = list(range(65, 81)) + list(range(97, 123))
        symbol_range_list = list(range(48, 58))
        return self.gen_pass(symbol_range_list, word_range_list)

    def pick_numbers(self, length, range_list):
        num_list = []
        for x in range(length):
            num_list.append(random.choice(range_list))
        return num_list

    def create_pass_list(self, symbol_range_list, word_range_list):
        return self.pick_numbers(self.len // self.dist, symbol_range_list) + self.pick_numbers(self.len - self.len // self.dist, word_range_list)


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


def copy_clipboard():
    root.clipboard_clear()
    root.clipboard_append(str(password.get()))
    root.update()


mainframe = ttk.Frame(root, padding='25 25 25 25')
mainframe.grid()
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

symb_bool = BooleanVar()
length = StringVar()
password = StringVar()
dist = StringVar()

length_entry = ttk.Entry(mainframe, width=7, textvariable=length)
length_entry.grid(column=2, row=1, sticky=(W, E))

dist_entry = ttk.Entry(mainframe, width=25, textvariable=dist)
dist_entry.grid(column=2, row=2, sticky=(W, E))


password_entry = ttk.Entry(mainframe, width=25, textvariable=password)
password_entry.grid(column=2, row=3, sticky=(W, E))
password_entry.config(state='readonly')

ttk.Button(mainframe, text='Generate', command=create_object).grid(column=4, row=3, sticky=W)
ttk.Button(mainframe, text='Copy to clipboard', command=copy_clipboard).grid(column=4, row=4, sticky=W)


ttk.Label(mainframe, text='Password length').grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text='Generated password').grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text='Dist').grid(column=1, row=2, sticky=W)

rb1 = ttk.Radiobutton(mainframe, text='Symbols', variable=symb_bool, value=True)
rb1.grid(column=4, row=1, sticky=W)
rb1.invoke()
ttk.Radiobutton(mainframe, text='No symbols', variable=symb_bool, value=False).grid(column=4, row=2, sticky=W)


for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)


length_entry.focus()
root.bind('<Return>', create_object)
center_window(root)

root.mainloop()


