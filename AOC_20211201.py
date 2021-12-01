### First half
f = open("AOC_20211201.txt", "r")
inc = 0
prev = 0

for x in f:
    if int(x) > prev:
        inc += 1
    prev = int(x)
inc -= 1
print("Number of increased readings: " + str(inc))
f.close()

### Second half
f = open("AOC_20211201.txt", "r")
i = 0
a = 0
b = 0
c = 0
sumA = 0
sumB = 0
inc = 0
for x in f:
    if i == 0:
        a = int(x)
    elif i == 1:
        b = int(x)
    elif i == 2:
        c = int(x)
    else:
        sumA = a+b+c
        a = b
        b = c
        c = int(x)
       
        sumB = a+b+c
        if sumB > sumA:
            inc += 1
    i += 1
print("Number of increased sums: " + str(inc))   
f.close()         