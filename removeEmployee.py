import os
from Employee import Employee

def removeEmployee():
    if os.path.exists("venv/data/emp.txt"):
        deleteAnother = 't'
        nameToDel = 't'
        file = open("venv/data/emp.txt", "r")
        file2 = open("../Employee/venv/data/emp1.txt", "at")
        while deleteAnother != 'n' and nameToDel != 'q':
            i = 1
            j = True
            k = 1
            nameToDel = input("\nEnter Employee ID Number to remove\n")
            while j:
                while i <= 8:
                    txt = file.readline()
                    if not txt:
                        j = False
                        break
                    test = txt.split(": ")
                    txt1 = test[1].split('\n')
                    if nameToDel == txt1[0]:
                        txt = file.readline()
                        txt = file.readline()
                        txt = file.readline()
                        txt = file.readline()
                        txt = file.readline()
                        txt = file.readline()
                        txt = file.readline()
                        k -= 1
                        break
                    if test[0] == "Employee ID":
                        file2.write(test[0] + ": " + str(k) + "\n")
                    else:
                        file2.write(test[0] + ": " + txt1[0] + "\n")
                    i += 1
                i = 1
                k += 1
            file.close()
            os.remove("venv/data/emp.txt")
            deleteAnother = 'n'
        file2.close()

    elif os.path.exists("../Employee/venv/data/emp1.txt"):
        deleteAnother = 't'
        nameToDel = 't'
        file = open("../Employee/venv/data/emp1.txt", "r")
        file2 = open("venv/data/emp.txt", "at")
        while deleteAnother != 'n' and nameToDel != 'q':
            i = 1
            j = True
            k = 1
            nameToDel = input("\nEnter Employee ID Number to remove\n")
            while j:
                while i <= 8:
                    txt = file.readline()
                    if not txt:
                        j = False
                        break
                    test = txt.split(": ")
                    txt1 = test[1].split('\n')
                    if nameToDel == txt1[0]:
                        txt = file.readline()
                        txt = file.readline()
                        txt = file.readline()
                        txt = file.readline()
                        txt = file.readline()
                        txt = file.readline()
                        txt = file.readline()
                        k -= 1
                        break
                    if test[0] == "Employee ID":
                        file2.write(test[0] + ": " + str(k) + "\n")
                    else:
                        file2.write(test[0] + ": " + txt1[0] + "\n")
                    i += 1
                i = 1
                k += 1
            file.close()
            os.remove("../Employee/venv/data/emp1.txt")
            deleteAnother = 'n'
        file2.close()

    else:
        print("The file does not exist")