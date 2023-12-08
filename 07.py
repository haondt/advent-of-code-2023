import re, lib

def get_type_score(hand):
    counts = {}
    for card in hand:
        if card not in counts:
            counts[card] = 0
        counts[card] += 1
    counts = sorted(counts.values())

    # 5 of a kind
    match len(counts):
        case 1:
            return 'A'
        case 2:
            match counts:
                # 4 of a kind
                case [1, 4]:
                    return 'B'
                # full house
                case [2, 3]:
                    return 'C'
        case 3:
            match counts:
                # 3 of a kind
                case [1, 1, 3]:
                    return 'D'
                # 2 pair
                case [1, 2, 2]:
                    return 'E'
        case 4:
            # 1 pair
            if counts == [1, 1, 1, 2]:
                return 'F'
    # high card
    return 'G'

def get_card_score(hand, j_score='D'):
    score = ''
    weights = {
            'A': 'A',
            'K': 'B',
            'Q': 'C',
            'J': j_score,
            'T': 'E',
            '9': 'F',
            '8': 'G',
            '7': 'H',
            '6': 'I',
            '5': 'J',
            '4': 'K',
            '3': 'L',
            '2': 'M'
            }
    for card in hand:
        score += weights[card]
    return score

def compute_hand_score(hand):
    type_score = get_type_score(hand)
    card_score = get_card_score(hand)
    return type_score + card_score

def recursive_compute_possible_j_hands(hand):
    if hand == '':
        return [hand]
    hands = []
    current_card = hand[0]
    remaining_possibilities = recursive_compute_possible_j_hands(hand[1:])
    if current_card == 'J':
        for card in 'AKQJT98765432':
            hands += [card + c for c in remaining_possibilities]
    else:
        hands = [current_card + c for c in remaining_possibilities]
    return hands

def compute_j_hand_score(hand):
    type_score = min([get_type_score(h) for h in recursive_compute_possible_j_hands(hand)])
    card_score = get_card_score(hand, 'Z')
    return type_score + card_score

def part_1():
    s = lib.read().split('\n')
    s = [i.strip() for i in s]

    entries = [line.split(' ') for line in s]
    entries = sorted(entries, reverse=True, key=lambda entry: compute_hand_score(entry[0]))

    result = 0
    for rank, entry in enumerate(entries):
        _, bid = entry
        result += int(bid) * (rank + 1)
    return result

def part_2():
    s = lib.read().split('\n')
    s = [i.strip() for i in s]

    entries = [line.split(' ') for line in s]
    entries = sorted(entries, reverse=True, key=lambda entry: compute_j_hand_score(entry[0]))

    result = 0
    for rank, entry in enumerate(entries):
        _, bid = entry
        result += int(bid) * (rank + 1)
    return result



#result = part_1()
result = part_2()
print(result)
