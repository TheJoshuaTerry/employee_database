import os
from Employee import Employee


def addEmployee():
    if os.path.exists("venv/data/emp.txt"):
        file = open("venv/data/emp.txt", "r")
        file2 = open("../Employee/venv/data/emp1.txt", "at")
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
        file.close()
        os.remove("venv/data/emp.txt")
        print("Add employee?")
        addCheck = input("Y for Yes\\N for No\n")
        lowerAdd = addCheck.lower()
        while lowerAdd == "y":
            print("Add new Employee: \n")
            firstName = input("First Name: ")
            lastName = input("Last Name: ")
            age = input("Age: ")
            address = input("Address: ")
            phone = input("Phone Number: ")
            email = input("Email: ")
            dept = input("Department: ")
            salary = input("Salary: ")
            emp1 = Employee(firstName, lastName, age, address, phone, email, dept, salary)
            file2.write(
                "Employee ID: " + str(emp1.empID) + "\nName: " + emp1.firstName + " "
                + emp1.lastName + "\nAge: " + emp1.age + "\nAddress: " + emp1.address
                + "\nPhone Number: " + emp1.phoneNum + "\nEmail: " + emp1.email
                + "\nDepartment: " + emp1.dept + "\nSalary: " + emp1.salary + "\n")
            print("Add employee?")
            addCheck = input("Y for Yes\\N for No\n")
            lowerAdd = addCheck.lower()
            del emp1
        file2.close()

    elif os.path.exists("../Employee/venv/data/emp1.txt"):
        file = open("../Employee/venv/data/emp1.txt", "r")
        file2 = open("venv/data/emp.txt", "at")
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
        file.close()
        os.remove("../Employee/venv/data/emp1.txt")
        print("Add employee?")
        addCheck = input("Y for Yes\\N for No\n")
        lowerAdd = addCheck.lower()
        while lowerAdd == "y":
            print("Add new Employee: \n")
            firstName = input("First Name: ")
            lastName = input("Last Name: ")
            age = input("Age: ")
            address = input("Address: ")
            phone = input("Phone Number: ")
            email = input("Email: ")
            dept = input("Department: ")
            salary = input("Salary: ")
            emp1 = Employee(firstName, lastName, age, address, phone, email, dept, salary)
            file2.write(
                "Employee ID: " + str(emp1.empID) + "\nName: " + emp1.firstName + " "
                + emp1.lastName + "\nAge: " + emp1.age + "\nAddress: " + emp1.address
                + "\nPhone Number: " + emp1.phoneNum + "\nEmail: " + emp1.email
                + "\nDepartment: " + emp1.dept + "\nSalary: " + emp1.salary + "\n")
            print("Add employee?")
            addCheck = input("Y for Yes\\N for No\n")
            lowerAdd = addCheck.lower()
            del emp1
        file2.close()

    else:
        print("The file does not exist")
        file = open("venv/data/emp.txt", "at")
        print("Add employee?")
        addCheck = input("Y for Yes\\N for No\n")
        lowerAdd = addCheck.lower()
        while lowerAdd == "y":
            print("Add new Employee: \n")
            firstName = input("First Name: ")
            lastName = input("Last Name: ")
            age = input("Age: ")
            address = input("Address: ")
            phone = input("Phone Number: ")
            email = input("Email: ")
            dept = input("Department: ")
            salary = input("Salary: ")
            emp1 = Employee(firstName, lastName, age, address, phone, email, dept, salary)
            file.write(
                "Employee ID: " + str(emp1.empID) + "\nName: " + emp1.firstName + " "
                + emp1.lastName + "\nAge: " + emp1.age + "\nAddress: " + emp1.address
                + "\nPhone Number: " + emp1.phoneNum + "\nEmail: " + emp1.email
                + "\nDepartment: " + emp1.dept + "\nSalary: " + emp1.salary + "\n")
            print("Add employee?")
            addCheck = input("Y for Yes\\N for No\n")
            lowerAdd = addCheck.lower()
            del emp1
        file.close()