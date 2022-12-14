from lxml.doctestcompare import strip

# AoC Day 1 Part 1

data = open('./data/day1_1.txt', 'r')
content = data.readlines()

max = 0
current = 0

for line in content:
    if line != '\n':
        current += int(line)
    else:
        print(current, max)
        if current > max:
            max = current

        current = 0
    #current=0
print(max)

# AoC Day 1 Part 2
arr=[]
max = 0
current = 0
for line in content:
    if line != '\n':
        current += int(line)
    else:
        arr.append(current)
        current = 0
    #current=0
arr.sort(reverse=True)
print(arr)
print(sum(arr[0:3]))