import random

# Part 1
seeds = []
seed2soil = []
soil2fertiliser = []
fertiliser2water = []
water2light = []
light2temperature = []
temperature2humidity = []
humidity2location = []


class Storage:
    def __init__(self, dest_start, source_start, length):
        self.dest_start = int(dest_start)
        self.source_start = int(source_start)
        self.range_length = int(length)


with open('inputs/5.txt', 'r') as f:
    lines = f.readlines()

    all_locations = []

    start_seed2soil = False
    start_soil2fertiliser = False
    start_fertiliser2water = False
    start_water2light = False
    start_light2temperature = False
    start_temperature2humidity = False
    start_humidity2location = False

    for line in lines:
        if line.startswith('seeds:'):
            seeds = [int(i) for i in line.split(':')[1].split()]
        elif line.startswith('seed-to-soil'):
            start_seed2soil = True
        elif line.startswith('soil-to-fertilizer'):
            start_soil2fertiliser = True
        elif line.startswith('fertilizer-to-water'):
            start_fertiliser2water = True
        elif line.startswith('water-to-light'):
            start_water2light = True
        elif line.startswith('light-to-temperature'):
            start_light2temperature = True
        elif line.startswith('temperature-to-humidity'):
            start_temperature2humidity = True
        elif line.startswith('humidity-to-location'):
            start_humidity2location = True

        if start_seed2soil and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            seed2soil.append(Storage(dest_start, source_start, length))
        elif start_soil2fertiliser and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            soil2fertiliser.append(Storage(dest_start, source_start, length))
        elif start_soil2fertiliser and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            soil2fertiliser.append(Storage(dest_start, source_start, length))
        elif start_fertiliser2water and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            fertiliser2water.append(Storage(dest_start, source_start, length))
        elif start_water2light and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            water2light.append(Storage(dest_start, source_start, length))
        elif start_light2temperature and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            light2temperature.append(Storage(dest_start, source_start, length))
        elif start_temperature2humidity and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            temperature2humidity.append(Storage(dest_start, source_start, length))
        elif start_humidity2location and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            humidity2location.append(Storage(dest_start, source_start, length))

        if line.strip() == '':
            start_seed2soil = False
            start_soil2fertiliser = False
            start_fertiliser2water = False
            start_water2light = False
            start_light2temperature = False
            start_temperature2humidity = False
            start_humidity2location = False

    seed2soil.sort(key=lambda x: x.source_start, reverse=True)
    soil2fertiliser.sort(key=lambda x: x.source_start, reverse=True)
    fertiliser2water.sort(key=lambda x: x.source_start, reverse=True)
    water2light.sort(key=lambda x: x.source_start, reverse=True)
    light2temperature.sort(key=lambda x: x.source_start, reverse=True)
    temperature2humidity.sort(key=lambda x: x.source_start, reverse=True)
    humidity2location.sort(key=lambda x: x.source_start, reverse=True)

    for seed in seeds:
        # print('seed ', seed)
        for count, soil in enumerate(seed2soil):
            if soil.source_start <= seed:
                break

        if soil.source_start + soil.range_length < seed or seed < soil.source_start:
            soil = seed
        else:
            diff = seed - soil.source_start
            soil = soil.dest_start + diff
        # print('soil ', soil)

        for count, fertiliser in enumerate(soil2fertiliser):
            if fertiliser.source_start <= soil:
                break
        if fertiliser.source_start + fertiliser.range_length < soil or soil < fertiliser.source_start:
            fertiliser = soil
        else:
            diff = soil - fertiliser.source_start
            fertiliser = fertiliser.dest_start + diff
        # print('fertiliser ', fertiliser)

        for count, water in enumerate(fertiliser2water):
            if water.source_start <= fertiliser:
                break
        if water.source_start + water.range_length < fertiliser or fertiliser < water.source_start:
            water = fertiliser
        else:
            diff = fertiliser - water.source_start
            water = water.dest_start + diff
        # print('water ', water)

        for count, light in enumerate(water2light):
            if light.source_start <= water:
                break
        if light.source_start + light.range_length < water or water < light.source_start:
            light = water
        else:
            diff = water - light.source_start
            light = light.dest_start + diff
        # print('light ', light)

        for count, temperature in enumerate(light2temperature):
            if temperature.source_start <= light:
                break
        if temperature.source_start + temperature.range_length < light or light < temperature.source_start:
            temperature = light
        else:
            diff = light - temperature.source_start
            temperature = temperature.dest_start + diff
        # print('temperature ', temperature)

        for count, humidity in enumerate(temperature2humidity):
            if humidity.source_start <= temperature:
                break
        if humidity.source_start + humidity.range_length < temperature or temperature < humidity.source_start:
            humidity = temperature
        else:
            diff = temperature - humidity.source_start
            humidity = humidity.dest_start + diff
        # print('humidity ', humidity)

        for count, location in enumerate(humidity2location):
            if location.source_start <= humidity:
                break
        if location.source_start + location.range_length < humidity or humidity < location.source_start:
            location = humidity
        else:
            diff = humidity - location.source_start
            location = location.dest_start + diff
        # print('location ', location)

        all_locations.append(location)

    print(min(all_locations))





# Part 2
seeds = []
seed2soil = []
soil2fertiliser = []
fertiliser2water = []
water2light = []
light2temperature = []
temperature2humidity = []
humidity2location = []


class Storage:
    def __init__(self, dest_start, source_start, length):
        self.dest_start = int(dest_start)
        self.source_start = int(source_start)
        self.range_length = int(length)


with open('inputs/5.txt', 'r') as f:
    lines = f.readlines()

    all_locations = []

    lowest_location = 999999999999999999999999999

    start_seed2soil = False
    start_soil2fertiliser = False
    start_fertiliser2water = False
    start_water2light = False
    start_light2temperature = False
    start_temperature2humidity = False
    start_humidity2location = False

    for line in lines:
        if line.startswith('seeds:'):
            numbers = line.split(':')[1].split()
            numbers = [int(x) for x in numbers]
            seeds = [numbers[i:i+2] for i in range(0, len(numbers), 2)]
            print(seeds)
        elif line.startswith('seed-to-soil'):
            start_seed2soil = True
        elif line.startswith('soil-to-fertilizer'):
            start_soil2fertiliser = True
        elif line.startswith('fertilizer-to-water'):
            start_fertiliser2water = True
        elif line.startswith('water-to-light'):
            start_water2light = True
        elif line.startswith('light-to-temperature'):
            start_light2temperature = True
        elif line.startswith('temperature-to-humidity'):
            start_temperature2humidity = True
        elif line.startswith('humidity-to-location'):
            start_humidity2location = True

        if start_seed2soil and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            seed2soil.append(Storage(dest_start, source_start, length))
        elif start_soil2fertiliser and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            soil2fertiliser.append(Storage(dest_start, source_start, length))
        elif start_soil2fertiliser and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            soil2fertiliser.append(Storage(dest_start, source_start, length))
        elif start_fertiliser2water and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            fertiliser2water.append(Storage(dest_start, source_start, length))
        elif start_water2light and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            water2light.append(Storage(dest_start, source_start, length))
        elif start_light2temperature and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            light2temperature.append(Storage(dest_start, source_start, length))
        elif start_temperature2humidity and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            temperature2humidity.append(Storage(dest_start, source_start, length))
        elif start_humidity2location and len(line.split()) == 3:
            dest_start, source_start, length = line.split()
            humidity2location.append(Storage(dest_start, source_start, length))

        if line.strip() == '':
            start_seed2soil = False
            start_soil2fertiliser = False
            start_fertiliser2water = False
            start_water2light = False
            start_light2temperature = False
            start_temperature2humidity = False
            start_humidity2location = False

    seed2soil.sort(key=lambda x: x.source_start, reverse=True)
    soil2fertiliser.sort(key=lambda x: x.source_start, reverse=True)
    fertiliser2water.sort(key=lambda x: x.source_start, reverse=True)
    water2light.sort(key=lambda x: x.source_start, reverse=True)
    light2temperature.sort(key=lambda x: x.source_start, reverse=True)
    temperature2humidity.sort(key=lambda x: x.source_start, reverse=True)
    humidity2location.sort(key=lambda x: x.source_start, reverse=True)

    for initial_seed, length in seeds:
        print(initial_seed)
        seeds = list(range(initial_seed, initial_seed + length, 20))
        random.shuffle(seeds)
        for seed in seeds:
            # print('seed ', seed)
            for count, soil in enumerate(seed2soil):
                if soil.source_start <= seed:
                    break

            if soil.source_start + soil.range_length < seed or seed < soil.source_start:
                soil = seed
            else:
                diff = seed - soil.source_start
                soil = soil.dest_start + diff
            # print('soil ', soil)

            for count, fertiliser in enumerate(soil2fertiliser):
                if fertiliser.source_start <= soil:
                    break
            if fertiliser.source_start + fertiliser.range_length < soil or soil < fertiliser.source_start:
                fertiliser = soil
            else:
                diff = soil - fertiliser.source_start
                fertiliser = fertiliser.dest_start + diff
            # print('fertiliser ', fertiliser)

            for count, water in enumerate(fertiliser2water):
                if water.source_start <= fertiliser:
                    break
            if water.source_start + water.range_length < fertiliser or fertiliser < water.source_start:
                water = fertiliser
            else:
                diff = fertiliser - water.source_start
                water = water.dest_start + diff
            # print('water ', water)

            for count, light in enumerate(water2light):
                if light.source_start <= water:
                    break
            if light.source_start + light.range_length < water or water < light.source_start:
                light = water
            else:
                diff = water - light.source_start
                light = light.dest_start + diff
            # print('light ', light)

            for count, temperature in enumerate(light2temperature):
                if temperature.source_start <= light:
                    break
            if temperature.source_start + temperature.range_length < light or light < temperature.source_start:
                temperature = light
            else:
                diff = light - temperature.source_start
                temperature = temperature.dest_start + diff
            # print('temperature ', temperature)

            for count, humidity in enumerate(temperature2humidity):
                if humidity.source_start <= temperature:
                    break
            if humidity.source_start + humidity.range_length < temperature or temperature < humidity.source_start:
                humidity = temperature
            else:
                diff = temperature - humidity.source_start
                humidity = humidity.dest_start + diff
            # print('humidity ', humidity)

            for count, location in enumerate(humidity2location):
                if location.source_start <= humidity:
                    break
            if location.source_start + location.range_length < humidity or humidity < location.source_start:
                location = humidity
            else:
                diff = humidity - location.source_start
                location = location.dest_start + diff
            # print('location ', location)

            if location < lowest_location:
                lowest_location = location

            if random.random() < 0.00001: print('lowest so far: ', lowest_location)

print('_____________')
print(lowest_location)





