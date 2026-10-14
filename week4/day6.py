def make_check(min_count, min_len):
    return lambda word, n: len(word) > min_len and n>=min_count

def count_matching(counts,check):
    total=0
    for i,g in counts.items():
        if check(i,g):
            total+=1
    return total
count = {"мама": 5, "ела": 2, "кот": 7, 'я':4, 'Тролль':8}
print(count_matching(count, make_check(2,3)))
print(count_matching(count, make_check(5,2)))
