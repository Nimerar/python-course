sp=[]
while True:
    a=int(input(f'1.Add \n2.Remove \n3.Show \n4.sort\n0.exit '))
    if a==1:
        b=input('Товар: ')
        b=b.lower()
        if b in sp:
            print('Такой товар уже есть')
        else:
            sp.append(b)
    elif a==2:
        b=input('Какой товар удалить?')
        b=b.lower()
        if b in sp:
            sp.remove(b)
            print('Товар удален')
        else:
                print('Такого товара нет')
    elif a==3:
        count=0
        for i in sp:
            count+=1
            print (count ,i)
    elif a==4:
        sp.sort()
        print('Список отсортирован')
    elif a!=0 and a!=1 and a!=2 and a!=3 and a!=4:
        print('Такой операции нет')
    else:
        break
for i in sp:
    print(i)
print("Пока!")
