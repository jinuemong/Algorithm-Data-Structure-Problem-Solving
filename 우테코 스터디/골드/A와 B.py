s = input()
t = input()

while len(t) > len(s):
    if t[-1] == "A":
        t = t[:-1]
    elif t[-1] == "B":
        t = t[:-1][::-1]
    if t == s:

        break
if t==s :print(1)
else: print(0)
