def part_1():
    lines = []
    with open('input.txt') as f:
        lines = [l for l in f if len(l) > 0]
    s = 0
    for line in lines:
        if len(line) <= 0:
            continue
        first_ptr = 0
        last_ptr = len(line) - 1
        while first_ptr < len(line):
            if line[first_ptr].isdigit():
                break
            first_ptr += 1

        while last_ptr >= first_ptr:
            if line[last_ptr].isdigit():
                break
            last_ptr -= 1
        num = int(line[first_ptr] + line[last_ptr])
        s += num
    return s


def part_2():
    values = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            }
    lines = []
    lines = []
    with open('input.txt') as f:
        lines = [l for l in f if len(l) > 0]
    s = 0
    digit = ''
    for line in lines:
        def f1():
            for i in range(len(line)):
                for key, value in values.items():
                    if line[i:].startswith(key):
                        return f"{value}"
        def f2():
            for i in range(len(line), -1, -1):
                for key, value in values.items():
                    if line[:i].endswith(key):
                        return f"{value}"
        s += int(f"{f1()}{f2()}")
    return s

print(part_2())



