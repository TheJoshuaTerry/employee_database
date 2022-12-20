from addEmployee import add_employee
from removeEmployee import remove_employee
from viewEmployees import view_employee

print("         WELCOME TO THE EMPLOYEE DATABASE!!!     ")
print("This database allows you to View, Add, and Remove Employees")
check = input("A for Add | V for View | R for Remove | Q for Quit\n").lower()
while check != "q":
    if check == "a":
        add_employee()
        check = input("A for Add \\ V for View \\ R for Remove \\ Q for Quit\n").lower()
    elif check == "v":
        view_employee()
        check = input("A for Add \\ V for View \\ R for Remove \\ Q for Quit\n").lower()
    elif check == "r":
        view_employee()
        remove_employee()
        check = input("A for Add \\ V for View \\ R for Remove \\ Q for Quit\n").lower()