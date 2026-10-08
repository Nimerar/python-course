# sp=[1,3,5,6,5]
# sp=set(sp)
# print(sp)
# sp.add(7)
# sp.add(5)
# sp.discard(1)
# sp.discard(100)
# print(sp)
# print(len(sp))

# text='Мама дома ела кашу мама съеда кашу'.lower()
# new=set()
# count=0
# for i in text.split():
#     if i not in new:
#         count+=1
#         new.add(i)
# print (count, new)

nums = [4, 7, 1, 7, 4, 9]
word=set()
for i in nums:
    if i not in word:
        word.add(i)
    elif i in word:
        print(i)
        break
