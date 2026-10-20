
def clean_text (text,min_len=1):
    text2=[]
    text1=text.lower()
    text1=text1.replace(',','').replace('.','')
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

with open("message.txt", encoding="utf-8") as f:
    content = f.read()
print(count_words(content))
