def count_unique_character(a):
     t = ''
     for ch in a:
         if ch not in t:
              t += ch
     o=len(t)
     return o

ans=0
max_count_unique_character = 0
n=int(input())
for i in range(0,n):
   l=input()
   max_count_unique_character = max(count_unique_character(l), max_count_unique_character)
   
print(max_count_unique_character)
