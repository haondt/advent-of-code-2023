import lib
import re

def part_1():
    s = lib.read()
    result = 0
    for line in s.split('\n'):
        match = re.search(r'^Card\s+\d+: ([^|]+) \| ([^|]+)[^\d]*$', line)
        winning_numbers = match.group(1)
        your_numbers = match.group(2)
        clean = lambda l: [i.strip() for i in l if len(i.strip()) > 0]
        winning_numbers = set(clean(winning_numbers.split(' ')))
        your_numbers = clean(your_numbers.split(' '))

        matched_numbers_count = len([i for i in your_numbers if i in winning_numbers])
        score = 2**(matched_numbers_count-1) if matched_numbers_count > 0 else 0
        result += score
    return result

def part_2():
    s = lib.read()
    cards = {}
    for line in s.split('\n'):
        match = re.search(r'^Card\s+(\d+): ([^|]+) \| ([^|]+)[^\d]*$', line)
        card = int(match.group(1))
        winning_numbers = match.group(2)
        your_numbers = match.group(3)
        clean = lambda l: [i.strip() for i in l if len(i.strip()) > 0]
        winning_numbers = set(clean(winning_numbers.split(' ')))
        your_numbers = clean(your_numbers.split(' '))
        matched_numbers = [i for i in your_numbers if i in winning_numbers]
        cards[card] = len(matched_numbers)

    cache = {}
    def get_count_with_children(card_number) -> int:
        nonlocal cache
        if card_number in cache:
            return cache[card_number]
        if card_number not in cards:
            return 0
        copies = cards[card_number]
        result = 1
        for copy in range(card_number + 1, card_number + copies + 1):
            result += get_count_with_children(copy)
        cache[card_number] = result
        return result

    result = sum([get_count_with_children(k) for k in cards.keys()])
    return result


#result = part_1()
result = part_2()
print(result)

