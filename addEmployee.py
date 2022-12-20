import os
from Employee import Employee


def add(file):
    print("Add employee?")
    add_check = input("Y for Yes\\N for No\n")
    lower_add = add_check.lower()
    while lower_add == "y":
        print("Add new Employee: \n")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        age = input("Age: ")
        address = input("Address: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        dept = input("Department: ")
        salary = input("Salary: ")
        emp1 = Employee(first_name, last_name, age, address, phone, email, dept, salary)
        file.write(
            "Employee ID: " + str(emp1.empID) + "\nName: " + emp1.firstName + " "
            + emp1.lastName + "\nAge: " + emp1.age + "\nAddress: " + emp1.address
            + "\nPhone Number: " + emp1.phone_number + "\nEmail: " + emp1.email
            + "\nDepartment: " + emp1.dept + "\nSalary: " + emp1.salary + "\n")
        print("Add employee?")
        add_check = input("Y for Yes\\N for No\n")
        lower_add = add_check.lower()
        del emp1
    file.close()


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


def add_employee():
    if os.path.exists("data/emp.txt"):
        file = open("data/emp.txt", "r")
        file2 = open("data/emp1.txt", "at")
        copy_text(file, file2)
        file.close()
        os.remove("data/emp.txt")
        add(file2)

    elif os.path.exists("data/emp1.txt"):
        file = open("data/emp1.txt", "r")
        file2 = open("data/emp.txt", "at")
        copy_text(file, file2)
        file.close()
        os.remove("data/emp1.txt")
        add(file2)

    else:
        print("The file does not exist")
        file = open("data/emp.txt", "at")
        add(file)
