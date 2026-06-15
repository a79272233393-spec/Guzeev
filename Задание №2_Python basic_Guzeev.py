#вариант 1
s = 'bfgshbkis'
s = s.replace('bfgshbk','')
s = s[:1]+'b'+s[1:]
print(s)

#вариант 2
s2 = 'bfgshbkis'
s2 = s2[::-1]
print(s2[1:6:2])

