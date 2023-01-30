student = []





def PUSH():
    admno = int(input("Enter Admission number:"))
    name = input("Enter the name:")
    rec = [admno, name]
    student.append(rec)

def DISPLAY():
    if student == []:
       print("Empty Stack")
    else:
       for st in student:
        if st[1][0] == 'A':
            print(st[0], st[1])



print("PUSHING")
for a in range (5):
    PUSH()

DISPLAY()