class Person:
    def __init__(self, f_name, l_name, age, address, phone_num, email):
        self.firstName = f_name
        self.lastName = l_name
        self.age = age
        self.address = address
        self.phone_number = phone_num
        self.email = email

    def print_info(self):
        print("Name: ", self.firstName, self.lastName, "\nAge: ", self.age,
              "\nAddress: ", self.address, "\nPhone Number: ", self.phone_number, "\nEmail: ", self.email)


class Employee(Person):
    empCount = 0
    empID = 1

    def __init__(self, f_name, l_name, age, address, phone_num, email, dept, salary):
        super().__init__(f_name, l_name, age, address, phone_num, email)
        self.dept = dept
        self.salary = salary
        self.empID = Employee.empID
        Employee.empCount += 1
        Employee.empID += 1

    def print_info(self):
        print("Name: ", self.firstName, self.lastName, "\nAge: ", self.age,
              "\nAddress: ", self.address, "\nPhone Number: ", self.phone_number, "\nEmail: ", self.email,
              "\nDept: ", self.dept, "\nSalary: ", self.salary, "\nEmployee ID: ", self.empID)

