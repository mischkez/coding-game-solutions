# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

minX = 0
maxX = w - 1
minY = 0
maxY = h - 1

while True:
    bomb_dir = input() 

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    if bomb_dir[0] == "U": maxY = y0 - 1 
    if bomb_dir[0] == "D": minY = y0 + 1 
    if bomb_dir[-1] == "R": minX = x0 + 1
    if bomb_dir[-1] == "L": maxX = x0 - 1

    x0 = int( (minX + maxX) / 2)
    y0 = int( (minY + maxY) / 2 )
    
    # the location of the next window Batman should jump to.
    print(x0, y0)
