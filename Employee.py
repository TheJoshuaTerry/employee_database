class Person:
    def __init__(self, fname, lname, age, address, phoneNum, email):
        self.firstName = fname
        self.lastName = lname
        self.age = age
        self.address = address
        self.phoneNum = phoneNum
        self.email = email

    def printInfo(self):
        print("Name: ", self.firstName, self.lastName, "\nAge: ", self.age,
              "\nAddress: ", self.address, "\nPhone Number: ", self.phoneNum, "\nEmail: ", self.email)


class Employee(Person):
    empCount = 0
    empID = 1

    def __init__(self, fname, lname, age, address, phoneNum, email, dept, salary):
        super().__init__(fname, lname, age, address, phoneNum, email)
        self.dept = dept
        self.salary = salary
        self.empID = Employee.empID
        Employee.empCount += 1
        Employee.empID += 1

    def printInfo(self):
        print("Name: ", self.firstName, self.lastName, "\nAge: ", self.age,
              "\nAddress: ", self.address, "\nPhone Number: ", self.phoneNum, "\nEmail: ", self.email,
              "\nDept: ", self.dept, "\nSalary: ", self.salary, "\nEmployee ID: ", self.empID)

