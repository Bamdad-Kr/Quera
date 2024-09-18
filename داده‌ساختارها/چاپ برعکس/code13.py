s = []
for i in range(1000):
    a = int(input())
    if a == 0 :
        for i in range(len(s)-1, -1, -1): # changed
             print(s[i])
        break

    s.append(a) # changed
