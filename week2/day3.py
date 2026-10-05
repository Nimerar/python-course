# Students=[("Anya", 18), ("Misha", 19), ("Dacha", 20),("Arina",21)] #1
# for i in Students:
#     student = i
#     print (student)


sp=[1,-2,3,-4,5,-6]
for i in range (1,(len(sp)//2)+1):
    sp[i-1],sp[-i]=sp[-i],sp[i-1]
print(sp)

sp1=[1,-2,3,-4,5]
for i in range (1,(len(sp1)//2)+1):
    sp1[i-1],sp1[-i]=sp1[-i],sp1[i-1]
print(sp1)



# People=("Misha", 20) #2
# People(0)=="Anya"
