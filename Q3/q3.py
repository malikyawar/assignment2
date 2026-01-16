from collections import Counter

def findMostFrequentWord (inputList1: list [str], inputList2: list [str], excluded: list [str]) -> str:
    filtered = [w for w in inputList1 if w not in excluded]
    freq = Counter(filtered)
    items = list(freq.items())
    items.sort(
        key=lambda x: (x[1], inputList1[::-1].index(x[0])),
        reverse=True
    )
    return items[1][0]