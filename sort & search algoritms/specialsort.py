import re

line = input().strip()

lowers = re.findall(r"[a-z]", line)
lowers.sort()

uppers = re.findall(r"[A-Z]", line)
uppers.sort()

odds = re.findall(r"[1,3,5,7,9]", line)
odds = list(map(int, odds))
odds.sort()

evens = re.findall(r"[0,2,4,6,8]", line)
evens = list(map(int, evens))
evens.sort()

print(*(lowers + uppers + odds + evens), sep="")