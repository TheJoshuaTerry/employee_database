import os
FILE_TXT = "data/emp.txt"
FILE1_TXT = "data/emp1.txt"


def view(file_txt):
    with open(file_txt, 'r') as file:
        txt = file.readline()
        if not txt:
            print("File empty \nDELETING FILE")
            file.close()
            os.remove(file_txt)
            return
        file.close()
        file = open(file_txt, "r")
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


def view_employee():
    if os.path.exists(FILE_TXT):
        view(FILE_TXT)

    elif os.path.exists(FILE1_TXT):
        view(FILE1_TXT)

