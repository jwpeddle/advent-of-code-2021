with open("input.txt") as f:
    lines = f.read().splitlines()

increased = 0
previous = None

for line in lines:
    if previous and int(line) > int(previous):
        increased += 1
    previous = line

print(increased)
