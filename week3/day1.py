grades={'Математкика':5,'Физика':4,'История':3}
while True:
    a=input("Введите название предмета ")
    if a in grades:
        print(a, grades[a])
    elif a=='0':
        break
    else:
        print('Такого предмета нет! ')

while True:
    b=input('Введите название предмета! ')
    if b=='0': break
    grade=grades.get(b)
    if grade is None: print('Нет такого предмета')
    else: print(grade)
