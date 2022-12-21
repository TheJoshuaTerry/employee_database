from tkinter import *
import os
from Employee import Employee
FILE_TXT = "data/emp.txt"
FILE1_TXT = "data/emp1.txt"


class ViewWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('300x100')
        self.minsize(width=400, height=500)
        self.config(padx=30, pady=30)
        self.title('Employee Database')
        self.attrib_list = []
        self.counter = 0
        self.lines = 0
        self.first_name_entry = Label(self)
        self.first_name_entry.grid(column=1, row=1)
        self.age_entry = Label(self)
        self.age_entry.grid(column=1, row=3, pady=5)
        self.phone_num_entry = Label(self)
        self.phone_num_entry.grid(column=1, row=4, pady=5)
        self.email_entry = Label(self)
        self.email_entry.grid(column=1, row=5, pady=5)
        self.street_entry = Label(self)
        self.street_entry.grid(column=1, row=6, pady=5)
        self.dept_entry = Label(self)
        self.dept_entry.grid(column=1, row=10, pady=5)
        self.salary_entry = Label(self)
        self.salary_entry.grid(column=1, row=11, pady=5)
        window_label = Label(self, text='View Employee', font=('Comic Sans', 24))
        window_label.grid(column=1, row=0, pady=5)
        self.view_employee()
        self.window()

        # Close Button
        Button(self, text='Close', command=self.destroy).grid(column=1, row=12)

        # Next Button
        Button(self, text='Next', command=self.next).grid(column=2, row=12)

        # Previous Button
        Button(self, text='Previous', command=self.previous).grid(column=0, row=12)

    def view(self, file_txt):
        with open(file_txt, 'r') as file:
            txt = file.readline()
            if not txt:
                print("File empty \nDELETING FILE")
                file.close()
                os.remove(file_txt)
                return
            file.close()
            file = open(file_txt, "r")
            i = 1
            j = True
            k = 0
            while j:
                while i <= 8:
                    txt = file.readline()
                    if not txt:
                        j = False
                        break
                    test = txt.split(": ")
                    txt1 = test[1].split('\n')
                    self.lines += 1
                    self.attrib_list.append(txt1[0])
                    i += 1
                i = 1

    def window(self):
        # Name
        first_name_label = Label(self, text='Name:')
        first_name_label.grid(column=0, row=1)
        self.first_name_entry = Label(self, text=self.attrib_list[1 + self.counter])
        self.first_name_entry.grid(column=1, row=1)

        # Age
        age_label = Label(self, text='Age:')
        age_label.grid(column=0, row=3, pady=5)
        self.age_entry = Label(self, text=self.attrib_list[2 + self.counter])
        self.age_entry.grid(column=1, row=3, pady=5)

        # Phone Number
        phone_num_label = Label(self, text='Phone Number:')
        phone_num_label.grid(column=0, row=4, pady=5)
        self.phone_num_entry = Label(self, text=self.attrib_list[3 + self.counter])
        self.phone_num_entry.grid(column=1, row=4, pady=5)

        # Email
        email_label = Label(self, text='Email:')
        email_label.grid(column=0, row=5, pady=5)
        self.email_entry = Label(self, text=self.attrib_list[4 + self.counter])
        self.email_entry.grid(column=1, row=5, pady=5)

        # Address
        street_label = Label(self, text='Street Address:')
        street_label.grid(column=0, row=6, pady=5)
        self.street_entry = Label(self, text=self.attrib_list[5 + self.counter])
        self.street_entry.grid(column=1, row=6, pady=5)

        # Department
        dept_label = Label(self, text='Department:')
        dept_label.grid(column=0, row=10, pady=5)
        self.dept_entry = Label(self, text=self.attrib_list[6 + self.counter])
        self.dept_entry.grid(column=1, row=10, pady=5)

        # Salary
        salary_label = Label(self, text='Salary:')
        salary_label.grid(column=0, row=11, pady=5)
        self.salary_entry = Label(self, text=self.attrib_list[7 + self.counter])
        self.salary_entry.grid(column=1, row=11, pady=5)

    def view_employee(self):
        if os.path.exists(FILE_TXT):
            self.view(FILE_TXT)

        elif os.path.exists(FILE1_TXT):
            self.view(FILE1_TXT)

    def next(self):
        if self.counter + 10 <= self.lines:
            self.counter += 8
            self.first_name_entry.after(10, self.first_name_entry.destroy())
            self.age_entry.after(10, self.age_entry.destroy())
            self.phone_num_entry.after(10, self.phone_num_entry.destroy())
            self.email_entry.after(10, self.email_entry.destroy())
            self.street_entry.after(10, self.street_entry.destroy())
            self.dept_entry.after(10, self.dept_entry.destroy())
            self.salary_entry.after(10, self.salary_entry.destroy())
            self.window()

    def previous(self):
        if self.counter >= 8:
            self.counter -= 8
            self.first_name_entry.after(10, self.first_name_entry.destroy())
            self.age_entry.after(10, self.age_entry.destroy())
            self.phone_num_entry.after(10, self.phone_num_entry.destroy())
            self.email_entry.after(10, self.email_entry.destroy())
            self.street_entry.after(10, self.street_entry.destroy())
            self.dept_entry.after(10, self.dept_entry.destroy())
            self.salary_entry.after(10, self.salary_entry.destroy())
            self.window()
