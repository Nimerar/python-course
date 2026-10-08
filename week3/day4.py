text='Мама дома ела кашу мама съеда кашу'.lower()
text1={'a':1,'b':2,'c':3}
squares = [x * x for x in range(1, 11)] ; print (squares) #1
sp=[x for x in range (1,31) if x%3==0] ; print(sp) #2
sp1={len(x) for x in text.split()} ;print(sp1) #3
sp2={x:len(x) for x in text.split() }; print(sp2) #4
sp3={Y:X for X,Y in text1.items()} ; print (sp3)
