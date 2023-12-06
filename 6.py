
# Part 1
with open('inputs/6.txt') as f:
    lines = f.readlines()
    times = lines[0].split('Time: ')[1].split()
    distances = lines[1].split('Distance: ')[1].split()

    times = [int(x) for x in times]
    distances = [int(x) for x in distances]

    multiplication = 1
    for i in range(len(times)):
        fastest_times = []
        for t in range(times[i]):
            v = 1 * t
            d = v * (times[i] - t)
            if d > distances[i]:
                fastest_times.append(d)
        multiplication *= len(fastest_times)

    print(multiplication)



# Part 2
with open('inputs/6.txt') as f:
    lines = f.readlines()
    time = int(lines[0].split('Time: ')[1].replace(' ', ''))
    distance = int(lines[1].split('Distance: ')[1].replace(' ', ''))

    fastest_times = []
    for t in range(time):
        v = 1 * t
        d = v * (time - t)
        if d > distance:
            fastest_times.append(d)

    print(len(fastest_times))
