import re


# Part 1
with open('inputs/4.txt') as f:
    total_points = 0
    for line in f:
        pattern = '^Card\s+(\d+):\s([\d+\s+]+)\|\s([\d+\s+]+)$'
        match = re.search(pattern, line)

        winning_numbers = [int(x) for x in match.group(2).split()]
        submitted_numbers = [int(x) for x in match.group(3).split()]

        total_winning_numbers = len([x for x in submitted_numbers if x in winning_numbers])

        if total_winning_numbers:
            total_points += 2**(total_winning_numbers - 1)


    print(total_points)



# Part 2
card_count_dict = dict()
total_cards = 0
with open('inputs/4.txt') as f:
    lines = f.readlines()
    total_lines = len(lines)

    for i in range(1, total_lines + 1):
        card_count_dict[i] = 1

    total_points = 0
    for count, line in enumerate(lines, 1):
        pattern = '^Card\s+(\d+):\s([\d+\s+]+)\|\s([\d+\s+]+)$'
        match = re.search(pattern, line)
        card_number = int(match.group(1))

        print('Card', card_number)
        winning_numbers = [int(x) for x in match.group(2).split()]
        submitted_numbers = [int(x) for x in match.group(3).split()]

        total_winning_numbers = len([x for x in submitted_numbers if x in winning_numbers])

        for _ in range(card_count_dict[card_number]):
            # print(count, card_number, total_winning_numbers)
            if total_winning_numbers:

                for i in range(1, total_winning_numbers+1):
                    try:
                        card_count_dict[count + i] = card_count_dict[count + i] + 1
                    except KeyError:
                        pass

            total_cards += 1



    print(total_cards)