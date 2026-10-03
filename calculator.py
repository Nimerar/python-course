while True:
    a=float(input(("Первое число ")))
    op= input("Операция на выбор: +,-,*,/ ")
    b=float(input("Второе число "))
    if op=="-":
        print(a-b )
    elif op=="*":
        print (a*b )
    elif op=="+":
        print(a+b )
    elif op=='/':
        if b==0:
            print ("Нельзя делить на 0")
        else:
            print(a/b)
    else:
        print("Неизвестная операция")
    c=input("Продолжить: Да/Нет ")
    c=c.lower()
    if c == "нет":
        break
