marks = []





def PUSH(m):
    marks.append(m)

def POP():
    if marks == []:
       print("Empty Stack")
    else:
       p = marks.pop()
       print(p)




print("PUSHING")
for a in range (5):
    num = int(input("Enter the number: "))
    PUSH(num)

print("POPPING")
for a in range(6):
    POP()