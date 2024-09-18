n = int(input())
names_count = {}

for i in range(n):
    first_name, last_name = input().split()
    if first_name in names_count:
        names_count[first_name] += 1
    else:
        names_count[first_name] = 1

max_duplicates = max(names_count.values(), default=1)
print(max_duplicates)
