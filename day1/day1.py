with open('input.txt', 'r') as file:
    lines = file.readlines()


def part_one():
    result = 0

    for word in lines:
        first_value = None
        last_value = None

        for char in word:
            if char.isdigit():
                last_value = char

                if not first_value:
                    first_value = char

        result += int(first_value + last_value)


def part_two():
    result = 0
    word_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    for word in lines:
        first_value = None
        last_value = None
        temp_string = str()

        for char in word:
            curr = None

            if char.isdigit():
                curr = char

            else:
                temp_string += char

                for key, value in word_map.items():
                    if temp_string.endswith(key):
                        curr = str(value)

            if curr:
                last_value = curr

                if not first_value:
                    first_value = curr

        result += int(first_value + last_value)
    print(result)
