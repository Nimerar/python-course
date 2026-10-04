Grades=[]
sum=0
count=0
fife=0
avg=0
while True:
    text=input("Оценка (Если закончились - enter)")
    if text == "":
        break
    Grade=int(text)
    if 2<= Grade <=5:
        Grades.append(Grade)
    else:
        print('Недопустимые значения')
if Grades == []:
    print("Оценок нет")
else:
    for i in Grades:
        sum+=i
        count+=1
        if i == 5: fife+=1
    avg=sum/count
    print(f"Оценки: {Grades}")
    print(f"Количество пятерок {fife}")
    print(f"Средний балл {avg}")
