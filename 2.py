import re


class Game:
    def __init__(self, game_id, red, blue, green):
        self.game_id = int(game_id)
        self.red = int(red)
        self.blue = int(blue)
        self.green = int(green)


def get_highest_number(lines):
    return max([int(line.split()[0]) for line in lines])


# Part 1
all_games = []
with open('inputs/2.txt') as f:
    for line in f:
        game_id = re.findall('Game (\d+):', line)[0]

        highest_blue = get_highest_number(re.findall('(\d+) blue', line))
        highest_green = get_highest_number(re.findall('(\d+) green', line))
        highest_red = get_highest_number(re.findall('(\d+) red', line))

        all_games.append(Game(game_id, highest_red, highest_blue, highest_green))

    game_id_sum = 0
    for game in all_games:
        if game.red <= 12 and game.green <= 13 and game.blue <= 14:
            game_id_sum += game.game_id

    print(game_id_sum)


# Part 2
all_games = []
with open('inputs/2.txt') as f:
    for line in f:
        game_id = re.findall('Game (\d+):', line)[0]

        highest_blue = get_highest_number(re.findall('(\d+) blue', line))
        highest_green = get_highest_number(re.findall('(\d+) green', line))
        highest_red = get_highest_number(re.findall('(\d+) red', line))

        all_games.append(Game(game_id, highest_red, highest_blue, highest_green))

    game_sum = 0
    for game in all_games:
        game_sum += game.red * game.green * game.blue

    print(game_sum)
