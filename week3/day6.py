text = 'Мама сшила мне штаны, мама приготовила папе еду, мне подарили новый красивый телефон мне'.lower()
text=text.replace(',','')
count={}
for i in text.split():
    count[i]=count.get(i,0)+1
print(count)
print(len(set(text.split())))
best=max(count.values())
print(best)
sp={word:total1 for word, total1 in count.items() if best<=total1}; print(sp)
sp1={word:total1 for word, total1 in count.items() if 2<=total1}; print(sp1)
