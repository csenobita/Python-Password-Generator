import random
from tkinter import *

from random import *
from tkinter import StringVar, messagebox
from typing import Type


class PasswordGenerator:

    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("1000x800+400+100")
        self.fbg = '#658ddd'
        self.len_var = StringVar()
        self.password_var = StringVar()

        self.font = ("Arial", 30, 'bold')
        self.font1 = ("Arial", 15, 'bold')
        self.frame = Frame(self.root, width=1000, height=800, bd=12, relief=GROOVE, bg=self.fbg)
        self.frame.pack()

        self.title_label = Label(self.frame, text="Password Generator", bd=0, font=self.font, bg=self.fbg, relief=RIDGE)
        self.title_label.place(x=300, y=20)

        self.password_label = Label(self.frame, text="Enter your password lent (8 to 32): ", bd=0, font=self.font1,
                                    bg=self.fbg, relief=RIDGE)
        self.password_label.place(x=100, y=200)

        self.password_entry = Entry(self.frame, bd=0, font=self.font1, textvariable=self.len_var, relief=RIDGE, width=4,
                                    justify='center')
        self.password_entry.place(x=500, y=200)

        self.generator_button = Button(self.frame, justify='center', cursor='hand2', text='Generate', bd=0,
                                       font=self.font1, bg=self.fbg, command=self.generate_password)
        self.generator_button.place(x=700, y=200)

        self.output = Text(self.frame, bd=0, width=40, height=10, font=self.font1, relief=RIDGE)
        self.output.place(x=300, y=400)

    def generate_password(self):
        self.output.config(state=NORMAL)
        len = int(self.len_var.get())
        self.output.delete(1.0,END)
        if 8 <= len <= 32:
            st = "asdfghjklzxcvbnmqwertyuiop1234567890@#$%&ASDFGHJKLQWERTYUIOPZXCVBNM"
            password = []

            for i in range(10):
                gen_password = choices(st, k=len)
                password.append(''.join(gen_password))
                #self.output.insert(END, "".join(gen_password))
            print(password)
            for char in password:
                self.output.insert(END,char)
                self.output.insert(END,'\n')
            self.output.config(state=DISABLED)
        else:
            messagebox.showerror('Error', 'Please enter a len(8-32 character password)')


if __name__ == '__main__':
    root = Tk()
    PasswordGenerator(root)
    root.mainloop()
