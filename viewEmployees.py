import os
from Employee import Employee

def viewEmployee():
    if os.path.exists("venv/data/emp.txt"):
        file = open("venv/data/emp.txt", "r")
        txt = file.readline()
        if not txt:
            print("File empty \nDELETING FILE")
            file.close()
            os.remove("venv/data/emp.txt")
            return
        file.close()
        file = open("venv/data/emp.txt", "r")
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
                print(test[0] + ": " + txt1[0])
                i += 1
            print("\n")
            i = 1
        file.close()
    elif os.path.exists("../Employee/venv/data/emp1.txt"):
        file = open("../Employee/venv/data/emp1.txt", "r")
        txt = file.readline()
        if not txt:
            print("File empty \nDELETING FILE")
            file.close()
            os.remove("../Employee/venv/data/emp1.txt")
            return
        file.close()
        file = open("../Employee/venv/data/emp1.txt", "r")
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
                print(test[0] + ": " + txt1[0])
                i += 1
            print("\n")
            i = 1
        file.close()