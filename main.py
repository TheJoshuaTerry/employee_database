
from addEmployee import addEmployee
from removeEmployee import removeEmployee
from viewEmployees import viewEmployee

print("         WELCOME TO THE EMPLOYEE DATABASE!!!     ")
print("This database allows you to View, Add, and Remove Employees")
check = input("A for Add | V for View | R for Remove | Q for Quit\n")
lowerCheck = check.lower()
while lowerCheck != "q":
    while lowerCheck == "a":
        addEmployee()
        check = input("A for Add \\ V for View \\ R for Remove \\ Q for Quit\n")
        lowerCheck = check.lower()
    while lowerCheck == "v":
        viewEmployee()
        check = input("A for Add \\ V for View \\ R for Remove \\ Q for Quit\n")
        lowerCheck = check.lower()
    while lowerCheck == "r":
        viewEmployee()
        removeEmployee()
        check = input("A for Add \\ V for View \\ R for Remove \\ Q for Quit\n")
        lowerCheck = check.lower()
