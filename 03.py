def read():
    lines = []
    with open('input.txt') as f:
        for line in f:
            if len(line) > 0:
                lines.append(line.strip())
    return '\n'.join(lines)

def flatten(l):
    return [i for j in l for i in j]

class Schematic:
    def __init__(self, matrix) -> None:
        self._matrix = matrix
    def get_surroundings(self, x: int, y: int, omit=[]) -> list[int|None]:
        coords = self.get_surrounding_coordinates(x, y, omit)
        return [self._matrix[y][x] for x, y in coords]
    def get_surrounding_coordinates(self, x: int, y: int, omit=[]) -> list[tuple[int, int]]:
        surroundings = []
        for hor_dir in [-1, 0, 1]:
            for ver_dir in [-1, 0, 1]:
                if hor_dir == 0 and ver_dir == 0:
                    continue
                new_x = x + hor_dir
                new_y = y + ver_dir
                if new_x < 0 or new_x >= len(self._matrix[0]):
                    continue
                if new_y < 0 or new_y >= len(self._matrix):
                    continue
                surroundings.append((new_x, new_y))
        surroundings = [c for c in surroundings if c not in omit]
        return surroundings

    def get_gear_ratios(self):
        numbers = []
        for y, row in enumerate(self._matrix):
            in_number = False
            num_start = 0
            for x, col in enumerate(row):
                if col.isdigit():
                    if not in_number:
                        num_start = x
                        in_number = True
                else:
                    if in_number:
                        numbers.append((y, num_start, x-1))
                        in_number = False

            if in_number:
                numbers.append((y, num_start, len(row)-1))

        gears = {}
        for number in numbers:
            digits = self._matrix[number[0]][number[1]:number[2]+1]
            value = int(digits)
            srd = []
            omit = [(x, number[0]) for x in range(number[1], number[2]+1)]
            srd = set(flatten([self.get_surrounding_coordinates(x, y, omit) for x, y in omit]))
            for x, y in srd:
                if self._matrix[y][x] == '*':
                    if (x, y) not in gears:
                        gears[(x, y)] = [value]
                    else:
                        gears[(x, y)].append(value)
        gears = {k:v for k, v in gears.items() if len(v) == 2}
        return [v[0] * v[1] for v in gears.values()]
    
    def get_part_numbers(self):
        numbers = []
        for y, row in enumerate(self._matrix):
            in_number = False
            num_start = 0
            for x, col in enumerate(row):
                if col.isdigit():
                    if not in_number:
                        num_start = x
                        in_number = True
                else:
                    if in_number:
                        numbers.append((y, num_start, x-1))
                        in_number = False

            if in_number:
                numbers.append((y, num_start, len(row)-1))

        part_numbers = []
        for number in numbers:
            digits = self._matrix[number[0]][number[1]:number[2]+1]
            value = int(digits)
            srd = []
            omit = [(x, number[0]) for x in range(number[1], number[2]+1)]
            srd = flatten([self.get_surroundings(x, y, omit) for x, y in omit])
            if any([i != '.' for i in srd]):
                part_numbers.append(value)

        return part_numbers

def part_1():
    sch = Schematic(read().split('\n'))
    numbers = sch.get_part_numbers()
    return sum(numbers)

def part_2():
    sch = Schematic(read().split('\n'))
    ratios = sch.get_gear_ratios()
    return sum(ratios)


#result = part_1()
result = part_2()
print(result)



