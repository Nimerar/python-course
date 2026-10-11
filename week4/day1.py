
text = 'Мама сшила мне штаны, мама приготовила папе еду, мне подарили новый красивый телефон мне'
def count_words (text):
    text=text.lower()
    text=text.replace(',','')
    counts={}
    for word in text.split():
        counts[word]=counts.get(word,0)+1
    return counts
w=count_words(text)
print(w)
q='Да да да'
q_counts=count_words(q)
print(q_counts)
