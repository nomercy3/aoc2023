from functools import reduce

with open('input.txt', 'r') as file:
    lines = file.readlines()


def part_one():
    max_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }

    game_ids = []
    for line in lines:
        line = line.replace('\n', '')
        game_id = line.split(' ')[1][:-1]

        sets = line.split('; ')
        sets[0] = sets[0].split(': ')[1]

        invalid_games = []

        for cubes in sets:
            cubes_splitted = cubes.split(', ')

            for number_color in cubes_splitted:
                number = number_color.split(' ')[0]
                color = number_color.split(' ')[1]

                if int(number) > max_cubes[color]:
                    invalid_games.append(game_id)

        if game_id not in invalid_games:
            game_ids.append(int(game_id))

    print(sum(game_ids))


def part_two():

    powers = []
    for line in lines:
        line = line.replace('\n', '')

        min_cubes = {}

        sets = line.split('; ')
        sets[0] = sets[0].split(': ')[1]


        for cubes in sets:
            cubes_splitted = cubes.split(', ')

            for number_color in cubes_splitted:
                number = number_color.split(' ')[0]
                color = number_color.split(' ')[1]

                stored_number = min_cubes.get(color)
                if stored_number and int(number) > stored_number:
                    min_cubes[color] = int(number)
                elif not stored_number:
                    min_cubes[color] = int(number)

        power = reduce(lambda x, y: x*y, [value for _, value in min_cubes.items()])

        powers.append(power)

    print(sum(powers))
