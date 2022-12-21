import os
FILE_TXT = "data/emp.txt"
FILE1_TXT = "data/emp1.txt"


def remove(file_txt, file1_txt):
    file = open(file_txt, "r")
    file2 = open(file1_txt, "at")
    delete_another = 't'
    employee_to_del = 't'
    while delete_another != 'n' and employee_to_del != 'q':
        i = 1
        j = True
        k = 1
        employee_to_del = input("\nEnter Employee ID Number to remove\n")
        while j:
            while i <= 8:
                txt = file.readline()
                if not txt:
                    j = False
                    break
                test = txt.split(": ")
                txt1 = test[1].split('\n')
                if employee_to_del == txt1[0]:
                    for n in range(7):
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
        os.remove(file_txt)
        delete_another = 'n'
    file2.close()


def remove_employee():
    if os.path.exists(FILE_TXT):
        remove(FILE_TXT, FILE1_TXT)

    elif os.path.exists(FILE1_TXT):
        remove(FILE1_TXT, FILE_TXT)

    else:
        print("NO database file exists")
