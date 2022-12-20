import os


def view_employee():
    if os.path.exists("data/emp.txt"):
        file = open("data/emp.txt", "r")
        txt = file.readline()
        if not txt:
            print("File empty \nDELETING FILE")
            file.close()
            os.remove("data/emp.txt")
            return
        file.close()
        file = open("data/emp.txt", "r")
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
    elif os.path.exists("data/emp1.txt"):
        file = open("data/emp1.txt", "r")
        txt = file.readline()
        if not txt:
            print("File empty \nDELETING FILE")
            file.close()
            os.remove("data/emp1.txt")
            return
        file.close()
        file = open("data/emp1.txt", "r")
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
