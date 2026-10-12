def count_words (text):
    text=text.lower()
    text=text.replace(',','')
    counts={}
    for word in text.split():
        counts[word]=counts.get(word,0)+1
    return counts
text='Мама мама Маммма мама ела ела ела '


def words_counts (text, min_counts=2):
    lent=len(text.split())
    new={}
    text=count_words(text)
    sum_unice=0
    for words1,total in text.items():
        sum_unice+=1
        if total>=min_counts:
            new[words1]=total
    return new, sum_unice, lent
print(words_counts(text))
