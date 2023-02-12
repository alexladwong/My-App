from tkinter import *
from random import randint
from tkinter import Entry

root = Tk()
root.title('Ladwong.org_StrongPasswordGenerator')
#root.iconbitmap(Image/icon_128x128.png)
root.geometry('500x230')


def new_rand():
    pw_entry.delete(0, END)

    pw_length = int(my_entry.get())

    my_password = ''

    for x in range(pw_length):
        my_password += chr * randint(33, 126)

    pw_entry.insert(0, my_password)


def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())


lf = LabelFrame(root, text="How Many Characters do you want?")
lf.pack(pady=20)

#my_entry + Entry(lf, font=("space mono", 18), bd=0, bg="white")
#my_entry.pack(pady=20, padx=20)

pw_entry = Entry(root, text='', font=("space mono", 28))
pw_entry.pack(pady=20)

my_frame = Frame(root)
my_frame.pack(pady=20)

my_button = Button(my_frame, text="Generate New Password", command=new_rand)
my_button.grid(row=5, column=0, padx=20)

clip_button = Button(my_frame, text="Copy to Clipboard", command=clipper)
clip_button.grid(row=4, column=0, padx=10)

root.mainloop()
