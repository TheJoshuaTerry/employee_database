from tkinter import *
import os
from Employee import Employee


class AddWindow(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry('300x100')
        self.minsize(width=400, height=500)
        self.config(padx=30, pady=30)
        self.title('Employee Database')
        window_label = Label(self, text='Add Employee', font=('Comic Sans', 24))
        window_label.grid(column=1, row=0, pady=5)

        # First Name input
        first_name_label = Label(self, text='First Name')
        first_name_label.grid(column=0, row=1)
        self.first_name_entry = Entry(self, width=15)
        self.first_name_entry.grid(column=1, row=1)

        # Last Name
        last_name_label = Label(self, text='Last Name')
        last_name_label.grid(column=0, row=2, pady=5)
        self.last_name_entry = Entry(self, width=15)
        self.last_name_entry.grid(column=1, row=2, pady=5)

        # Age
        age_label = Label(self, text='Age')
        age_label.grid(column=0, row=3, pady=5)
        self.age_entry = Entry(self, width=15)
        self.age_entry.grid(column=1, row=3, pady=5)

        # Phone Number
        phone_num_label = Label(self, text='Phone Number')
        phone_num_label.grid(column=0, row=4, pady=5)
        self.phone_num_entry = Entry(self, width=15)
        self.phone_num_entry.grid(column=1, row=4, pady=5)

        # Email
        email_label = Label(self, text='Email')
        email_label.grid(column=0, row=5, pady=5)
        self.email_entry = Entry(self, width=15)
        self.email_entry.grid(column=1, row=5, pady=5)

        # Street Address
        street_label = Label(self, text='Street Address')
        street_label.grid(column=0, row=6, pady=5)
        self.street_entry = Entry(self, width=30)
        self.street_entry.grid(column=1, row=6, pady=5)

        # City
        city_label = Label(self, text='City')
        city_label.grid(column=0, row=7, pady=5)
        self.city_entry = Entry(self, width=15)
        self.city_entry.grid(column=1, row=7, pady=5)

        # State
        state_label = Label(self, text='State')
        state_label.grid(column=0, row=8, pady=5)
        self.state_entry = Entry(self, width=15)
        self.state_entry.grid(column=1, row=8, pady=5)

        # Zip Code
        zipcode_label = Label(self, text='Zip Code')
        zipcode_label.grid(column=0, row=9, pady=5)
        self.zipcode_entry = Entry(self, width=15)
        self.zipcode_entry.grid(column=1, row=9, pady=5)

        # Department
        dept_label = Label(self, text='Department')
        dept_label.grid(column=0, row=10, pady=5)
        self.dept_entry = Entry(self, width=15)
        self.dept_entry.grid(column=1, row=10, pady=5)

        # Salary
        salary_label = Label(self, text='Salary')
        salary_label.grid(column=0, row=11, pady=5)
        self.salary_entry = Entry(self, width=15)
        self.salary_entry.grid(column=1, row=11, pady=5)

        # Submit Button
        submit_button = Button(self, text='Submit', command=self.create_data_txt)
        submit_button.grid(column=0, row=12)

        # Close Button
        Button(self, text='Close', command=self.destroy).grid(column=1, row=12)

    @staticmethod
    def copy_text(file, file2):
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
                file2.write(test[0] + ": " + txt1[0] + "\n")
                i += 1
            i = 1
            k += 1
        Employee.empID = k

    @staticmethod
    def add(file, first_name, last_name, age, address, phone, email, dept, salary):
        emp1 = Employee(first_name, last_name, age, address, phone, email, dept, salary)
        file.write(
            "Employee ID: " + str(emp1.empID) + "\nName: " + str(emp1.firstName) + " "
            + str(emp1.lastName) + "\nAge: " + str(emp1.age) + "\nAddress: " + emp1.address
            + "\nPhone Number: " + str(emp1.phone_number) + "\nEmail: " + str(emp1.email)
            + "\nDepartment: " + str(emp1.dept) + "\nSalary: " + str(emp1.salary) + "\n")
        del emp1
        file.close()

    def create_data_txt(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        age = self.age_entry.get()
        phone = self.phone_num_entry.get()
        email = self.email_entry.get()
        street = self.street_entry.get()
        city = self.city_entry.get()
        state = self.state_entry.get()
        zipcode = self.zipcode_entry.get()
        dept = self.dept_entry.get()
        salary = self.salary_entry.get()
        if os.path.exists("data/emp.txt"):
            file = open("data/emp.txt", "r")
            file2 = open("data/emp1.txt", "at")
            self.copy_text(file, file2)
            file.close()
            os.remove("data/emp.txt")
            self.add(file2, first_name=first_name, last_name=last_name, age=age,
                     address=f"{str(street)}, {str(city)}, {str(state)} {str(zipcode)}",
                     phone=f"{str(phone)}", email=f"{str(email)}", dept=f"{str(dept)}",
                     salary=f"{str(salary)}")

        elif os.path.exists("data/emp1.txt"):
            file = open("data/emp1.txt", "r")
            file2 = open("data/emp.txt", "at")
            self.copy_text(file, file2)
            file.close()
            os.remove("data/emp1.txt")
            self.add(file2, first_name=first_name, last_name=last_name, age=age,
                     address=f"{str(street)}, {str(city)}, {str(state)} {str(zipcode)}",
                     phone=f"{str(phone)}", email=f"{str(email)}", dept=f"{str(dept)}",
                     salary=f"{str(salary)}")

        else:
            print("The file does not exist")
            file = open("data/emp.txt", "at")
            self.add(file, first_name=first_name, last_name=last_name, age=age,
                     address=f"{str(street)}, {str(city)}, {str(state)} {str(zipcode)}",
                     phone=f"{str(phone)}", email=f"{str(email)}", dept=f"{str(dept)}",
                     salary=f"{str(salary)}")
        self.destroy()
