with open("input.txt") as f:
    lines = f.read().splitlines()

increased = 0
previous_sum = None

for i in range(0, len(lines)):
    try:
        group_sum = sum([
            int(lines[i]),
            int(lines[i+1]),
            int(lines[i+2])
        ])

        if previous_sum and group_sum > previous_sum:
            increased += 1
        previous_sum = group_sum

    except IndexError:
        pass

print(increased)
