fileObj = open("14.in", "r") #opens the file in read mode
lines = fileObj.read().splitlines() #puts the file into an array
fileObj.close()

zadanie = lines[0]

data = {}   # Dictionary 

for q in lines[2:]:   # Filling dictionary
    char_1, char_2 = q.split(" -> ")
    data[char_1] = char_2

for _ in range(40):
    n = zadanie[0]
    for c in zadanie[1:]:
        n += data[n[-1] + c]
        n += c
    zadanie = n

c = {}

for char in zadanie:
    if char not in c: 
        c[char] = 0
    c[char] += 1

print(max(c.values()) - min(c.values()))