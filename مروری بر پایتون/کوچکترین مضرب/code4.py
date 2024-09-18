inp = input()
inp = inp.split(" ")
p = int(inp[0])
q = int(inp[1])
t = 1
r = q % p

while r > (p/2):
	t = t+1
	r = (t*q)%p

print(q*t)
