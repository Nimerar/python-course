count={'мама':2,'ела':5}
def top_count (count):
    counts=max(count, key=count.get)
    maxim=max(count.values())
    return counts,maxim
print(top_count(count))
