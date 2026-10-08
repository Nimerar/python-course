# text='Мама дома ела кашу мама съеда кашу'.lower()
# count={}
# for word in text.split():
#     count[word] = count.get(word,0)+1
# print(count)
# print (text)
# Best_Word=None
# Best_Score=float('-inf')
# for word,total in count.items():
#     if Best_Score<=total:
#         Best_Score=total
#         Best_Word=word
# print(f'Лучший результат у слова: {Best_Word} с результатом {Best_Score}')
text = {'a':1,'b':2,'c':3}
new={}
for i,g in text.items():
    new[g]=i
print(new)
text1={'a':1,'b':1}
new1={}
for k,o in text1.items():
    new1[o]=k
print(new1)
