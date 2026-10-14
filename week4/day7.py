text='Мама ела кашу, мама съела и Сашку'
def clean_text (text,min_len=1):
    text2=[]
    text1=text.lower()
    text1=text1.replace(',','')
    for i in text1.split():
        if len(i)>=min_len:
            text2.append(i)
    return text2

def count_words(text):
    text=clean_text(text)
    count={}
    for word in text:
        count[word]=count.get(word,0)+1
    return count
print(count_words(text))

counts = count_words(text)

def count_word(counts):
    count=sorted (counts, key= lambda x: counts[x], reverse=True)
    return count
print(count_word(counts))

def longest_words(counts):
    return max(counts, key=lambda x: len(x))
print(longest_words(counts))
print(count)
