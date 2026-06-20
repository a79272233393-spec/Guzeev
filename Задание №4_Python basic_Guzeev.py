dct = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
dct2 = {}
for k,v in dct.items():
    if v>=3:
        dct2[k] = v
print(dct2)
