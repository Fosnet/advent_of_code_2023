from enum import Enum
from collections import Counter
import copy


class Rank(Enum):
    FIVE_OF_A_KIND = 'G'
    FOUR_OF_A_KIND = 'F'
    FULL_HOUSE = 'E'
    THREE_OF_A_KIND = 'D'
    TWO_PAIR = 'C'
    ONE_PAIR = 'B'
    HIGH_CARD = 'A'


hand_dict = {
    '2': '2',
    '3': '3',
    '4': '4',
    '5': '5',
    '6': '6',
    '7': '7',
    '8': '8',
    '9': '9',
    'T': ':',
    'J': ';',
    'Q': '<',
    'K': '=',
    'A': '>',
}


class Hand:
    def __init__(self, raw_cards, bid, j):
        self.card_values = []
        self.joker = j != ';'

        self.raw_cards = raw_cards
        self.get_rank(raw_cards)
        self.analyse_raw_data(raw_cards)
        self.bid = int(bid)

    def analyse_raw_data(self, s):
        string = ''
        for card in s:
            string += hand_dict[card]
        self.card_values = string

    def get_rank(self, cards):
        joker_present = 'J' in cards and self.joker

        number_of_iterations = 1 if not joker_present else len(hand_dict)

        rank_tracker = []
        for i in range(number_of_iterations):
            temp_cards = copy.deepcopy(cards)
            if number_of_iterations > 1:
                temp_cards = temp_cards.replace('J', list(hand_dict.keys())[i])

            counts = Counter(temp_cards)
            self.count_dict = dict()
            for i in temp_cards:
                self.count_dict[i] = counts[i]

            values = self.count_dict.values()
            value_counter = Counter(values)
            if max(values) == 5:
                self.rank = Rank.FIVE_OF_A_KIND
                rank_tracker.append(Rank.FIVE_OF_A_KIND.value)
                break
            elif max(values) == 4:
                self.rank = Rank.FOUR_OF_A_KIND
                rank_tracker.append(Rank.FOUR_OF_A_KIND.value)
            elif list(set(values)) == [2, 3]:
                self.rank = Rank.FULL_HOUSE
                rank_tracker.append(Rank.FULL_HOUSE.value)
            elif max(values) == 3:
                self.rank = Rank.THREE_OF_A_KIND
                rank_tracker.append(Rank.THREE_OF_A_KIND.value)
            elif value_counter[2] == 2:
                self.rank = Rank.TWO_PAIR
                rank_tracker.append(Rank.TWO_PAIR.value)
            elif value_counter[1] == 3:
                self.rank = Rank.ONE_PAIR
                rank_tracker.append(Rank.ONE_PAIR.value)
            elif max(values) == 1:
                self.rank = Rank.HIGH_CARD
                rank_tracker.append(Rank.HIGH_CARD.value)

        if number_of_iterations > 1:
            self.rank = Rank(max(rank_tracker))



for j in [';', '0']:
    with open('inputs/7.txt') as f:
        lines = f.readlines()

        hand_dict['J'] = j

        hands = []
        for line in lines:
            cards, bid = line.split()
            hands.append(Hand(cards, bid, j))

        five_of_a_kind = []
        four_of_a_kind = []
        full_house = []
        three_of_a_kind = []
        two_pair = []
        one_pair = []
        high_card = []
        for hand in hands:
            if hand.rank == Rank.FIVE_OF_A_KIND:
                five_of_a_kind.append(hand)
            elif hand.rank == Rank.FOUR_OF_A_KIND:
                four_of_a_kind.append(hand)
            elif hand.rank == Rank.FULL_HOUSE:
                full_house.append(hand)
            elif hand.rank == Rank.THREE_OF_A_KIND:
                three_of_a_kind.append(hand)
            elif hand.rank == Rank.TWO_PAIR:
                two_pair.append(hand)
            elif hand.rank == Rank.ONE_PAIR:
                one_pair.append(hand)
            elif hand.rank == Rank.HIGH_CARD:
                high_card.append(hand)
            else:
                print('FFFFFFFF')

        five_of_a_kind.sort(key=lambda x: x.card_values, reverse=True)
        four_of_a_kind.sort(key=lambda x: x.card_values, reverse=True)
        full_house.sort(key=lambda x: x.card_values, reverse=True)
        three_of_a_kind.sort(key=lambda x: x.card_values, reverse=True)
        two_pair.sort(key=lambda x: x.card_values, reverse=True)
        one_pair.sort(key=lambda x: x.card_values, reverse=True)
        high_card.sort(key=lambda x: x.card_values, reverse=True)

        all_hands = five_of_a_kind + four_of_a_kind + full_house + three_of_a_kind + two_pair + one_pair + high_card

        winnings = 0
        for count, hand in enumerate(reversed(all_hands), 1):
            winnings += hand.bid * count

        print(winnings)



