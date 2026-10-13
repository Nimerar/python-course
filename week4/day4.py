count={"мама":5,"ела":2}
def count_matching(counts,check):
    total=0
    for i,g in counts.items():
        if check(i,g):
            total+=1
    return total

def apply_to_all(func, items):
    return [func(x) for x in items]
print(apply_to_all(len, ['мама', 'ела']))
