count = {"мама": 5, "ела": 2, "кот": 7, 'я':4, 'Тролль':8}
def count_words(counts):
    count=sorted (counts, key= lambda x: counts[x], reverse=True)
    return count
print(count_words(count))


def longest_words(counts):
    return max(counts, key=lambda x: len(x))
print(longest_words(count))
