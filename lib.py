def read():
    lines = []
    with open('input.txt') as f:
        for line in f:
            if len(line) > 0:
                lines.append(line.strip())
    return '\n'.join(lines)

def flatten(l):
    return [i for j in l for i in j]
