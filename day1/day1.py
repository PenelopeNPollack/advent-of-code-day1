

with open('Advent_1.txt') as f:
    lines = f.readlines()

nums = [ int(line.strip()) for line in lines ]

for x in lines:
    for y in lines:

        x = int(x)
        y = int(y)


        if x+y == 2020:
            print(x*y)

for x in lines:
    for y in lines:
        for z in lines:
            x = int(x)
            y = int(y)
            z = int(z)

            if x+y+z == 2020:
                print(x*y*z)

f.close()