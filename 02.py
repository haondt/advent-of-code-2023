import re
def read():
    lines = []
    with open('input.txt') as f:
        for line in f:
            if len(line) > 0:
                lines.append(line.strip())
    return '\n'.join(lines)

def get_game_num(s):
    return re.search(r'Game (\d+):', s).group(1)

def get_sets(s):
    sets = re.search(r'Game (?:\d+): (.*)', s).group(1)
    sets = [i.strip() for i in sets.split(';')]
    return sets

def get_cubes(s):
    cubes = [i.strip() for i in s.split(',')]
    cubes = {i[1]:int(i[0]) for i in [j.split(' ') for j in cubes]}
    return cubes

def part_1():
    s = read()
    max_cubes = {}
    for line in s.split('\n'):
        game = get_game_num(line)
        max_cubes[game] = {}
        sets = get_sets(line)
        for _set in sets:
            cubes = get_cubes(_set)
            for color, quant in cubes.items():
                if color not in max_cubes[game]:
                    max_cubes[game][color] = quant
                else:
                    max_cubes[game][color] = max(quant, max_cubes[game][color])
    filter = {
            'red': 12,
            'green': 13,
            'blue': 14
            }
    def apply_filter(d):
        for key, value in d.items():
            if key not in filter:
                return False
            if value > filter[key]:
                return False
        return True

    return sum([int(k) for k, v in max_cubes.items() if apply_filter(v)])

def part_2():
    s = read()
    min_cubes = {}
    for line in s.split('\n'):
        game = get_game_num(line)
        min_cubes[game] = {}
        sets = get_sets(line)
        for _set in sets:
            cubes = get_cubes(_set)
            for color, quant in cubes.items():
                if color not in min_cubes[game]:
                    min_cubes[game][color] = quant
                else:
                    min_cubes[game][color] = max(quant, min_cubes[game][color])
    filter = {
            'red': 12,
            'green': 13,
            'blue': 14
            }
    def power(d): 
        p = 1
        for color in ['red', 'green', 'blue']:
            p *= d.get(color, 0)
        return p
    powers = [power(v) for v in min_cubes.values()]
    return sum(powers)

#result = part_1()
result = part_2()
print(result)


