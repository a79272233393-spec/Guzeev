
lst =  [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
def f(y):
    if y>50 and y%2==1:
        return True
print(list(filter(f, lst)))
print(list(sorted(filter(f,lst))))


