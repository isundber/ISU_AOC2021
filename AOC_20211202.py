### First half
f = open("AOC_20211202.txt", "r")
dpt = 0
fwd = 0

for x in f:
    line = x.split()
    if line[0] ==  'forward':
        fwd += int(line[1])
    elif line[0] == 'up':
        dpt -= int(line[1]) 
    else:
        dpt += int(line[1]) 
print("Multiplication result: "+str(dpt*fwd))
f.close()
### Second half
f = open("AOC_20211202.txt", "r")
dpt = 0
fwd = 0
aim = 0

for x in f:
    line = x.split()
    if line[0] ==  'forward':
        fwd += int(line[1])
        dpt += aim*int(line[1])
    elif line[0] == 'up':
        aim -= int(line[1])        
    else: 
        aim += int(line[1])
print("Multiplication result: "+str(dpt*fwd))
f.close() 