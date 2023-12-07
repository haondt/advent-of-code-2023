import lib

def get_distance(time, hold_time):
    speed = hold_time
    travel_time = time - hold_time
    distance = travel_time * speed
    return distance

def part_1():
    lines = lib.read().split('\n')
    times = [int(i) for i in lines[0].split(' ') if i.isdigit()]
    distances = [int(i) for i in lines[1].split(' ') if i.isdigit()]
    races = [(times[i], distances[i]) for i in range(len(times))]

    result = 1
    for time, distance in races:
        win_methods = 0
        for hold_time in range(0, time):
            potential_distance = get_distance(time, hold_time)
            winner = potential_distance > distance
            if winner:
                win_methods += 1
        result *= win_methods
    return result

def part_2():
    lines = lib.read().split('\n')
    time = int(''.join([i for i in lines[0].split(' ') if i.isdigit()]))
    distance = int(''.join([i for i in lines[1].split(' ') if i.isdigit()]))
    races = [(time, distance)]

    result = 1
    for time, distance in races:
        win_methods = 0
        for hold_time in range(0, time):
            potential_distance = get_distance(time, hold_time)
            winner = potential_distance > distance
            if winner:
                win_methods += 1
        result *= win_methods
    return result




#result = part_1()
result = part_2()
print(result)
