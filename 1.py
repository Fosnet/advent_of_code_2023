

numbers_dict_first_pass = {
    'one': 'one1one',
    'two': 'two2two',
    'three': 'three3three',
    'four': 'four4four',
    'five': 'five5five',
    'six': 'six6six',
    'seven': 'seven7seven',
    'eight': 'eight8eight',
    'nine': 'nine9nine'
}


# Part 1
total_sum = 0
with open('inputs/1.txt', 'r') as file:
    for count, line in enumerate(file):
        line_digits = ''

        for character in line:
            if character.isdigit():
                line_digits += character

        line_sum = int(line_digits[0] + line_digits[-1])

        total_sum += line_sum


print(total_sum)

# Part 2
total_sum = 0
with open('inputs/1.txt', 'r') as file:
    for count, line in enumerate(file):
        line_digits = ''

        for k in numbers_dict_first_pass:
            line = line.replace(k, numbers_dict_first_pass[k])

        for character in line:
            if character.isdigit():
                line_digits += character

        line_sum = int(line_digits[0] + line_digits[-1])

        total_sum += line_sum


print(total_sum)
