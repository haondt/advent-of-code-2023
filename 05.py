import re
from typing import final
import lib
from pathos.multiprocessing import Pool

class Map:
    def __init__(self, map_str):
        split_str = map_str.split(' ')
        self.source_start = int(split_str[1])
        self.source_end = self.source_start + int(split_str[2])
        self.conversion = int(split_str[0]) - self.source_start
    def try_convert(self, source):
        if source >= self.source_start and source <= self.source_end:
            return source + self.conversion
        return None

class Section:
    def __init__(self, map_strs):
        self.maps = [Map(i.strip()) for i in map_strs]

    def convert(self, source):
        for map in self.maps:
            result = map.try_convert(source)
            if result is not None:
                return result
        return source
    def get_map(self):
        return {(map.source_start, map.source_end + 1): map.conversion for map in self.maps}

def part_1():
    s = lib.read() 
    section_strs = s.split('\n\n')
    seeds = [int(i) for i in section_strs[0].strip().split(' ')[1:]]
    sections = {}
    for section_str in section_strs[1:]:
        lines = section_str.strip().split('\n')
        match = re.search(r'^(\w+)-to-(\w+) map:$', lines[0])
        source_type = match.group(1)
        dest_type = match.group(2)
        sections[source_type] = (dest_type, Section(lines[1:]))

    locations = []
    for seed in seeds:
        current_type = 'seed'
        current_value = seed
        while current_type != 'location':
            current_type, section = sections[current_type]
            current_value = section.convert(current_value) 
        locations.append(current_value)
    return min(locations)

# it took longer to figure this out than it took to brute force it... but the the brute force was off by one
# and this was quicker than trying to debug it
def combine_maps(base: dict[tuple[int, int], int], added: dict[tuple[int, int], int]):
    #print(base, added)
    final_base: dict[tuple[int, int], int] = {}
    for b_range, b_value in base.items():
        new_base: dict[tuple[int, int], int] = {}
        for a_range, a_value in added.items():
            i_range = (b_range[0] + b_value, b_range[1] + b_value)
            i_base: dict[tuple[int, int], int] = {}
            # check for overlap
            if a_range[0] < i_range[1] and a_range[1] >= i_range[0]:
                # split range
                mid = a_range[0]
                if a_range[0] < i_range[0]:
                    mid = i_range[0]
                    #new_base[(a_range[0] + 1, b_range[0])] = a_value
                #elif a_range[0] > i_range[0]:
                #    i_base[(i_range[0], a_range[0])] = 0

                if a_range[1] < i_range[1]:
                    i_base[(mid, a_range[1])] = a_value
                    #i_base[(a_range[1], i_range[1])] = 0
                elif a_range[1] >= i_range[1]:
                    i_base[(mid, i_range[1])] = a_value
                    #new_base[(b_range[1], a_range[1])] = a_value
                #else:
                    #i_base[(mid, a_range[1])] = a_value
            for k, v in i_base.items():
                new_base[(k[0] - b_value, k[1] - b_value)] = v + b_value
        #print('old', b_range)
        #print('new', new_base)

        ranges = sorted(new_base.keys())
        last_added_range = None
        if len(ranges) == 0:
            final_base[b_range] = b_value 
        else:
            for _range in ranges:
                if last_added_range is None:
                    if _range[0] > b_range[0]:
                        final_base[(b_range[0], _range[0])] = b_value
                    final_base[_range] = new_base[_range]
                else:
                    if _range[0] > last_added_range[1]:
                        final_base[(last_added_range[1], _range[0])] = b_value
                    final_base[_range] = new_base[_range]
                last_added_range = _range
            if last_added_range and last_added_range[1] < b_range[1]:
                final_base[(last_added_range[1], b_range[1])] = b_value
    return final_base

def apply_map(map, seed):
    for key, value in map.items():
        if seed >= key[0] and seed < key[1] - 1:
            return seed + value
    return None


def part_2():
    s = lib.read() 
    section_strs = s.split('\n\n')
    seeds = [int(i) for i in section_strs[0].strip().split(' ')[1:]]
    seeds = [(seeds[i], seeds[i+1] + 1) for i in range(0, len(seeds), 2)]
    sections = {}
    for section_str in section_strs[1:]:
        lines = section_str.strip().split('\n')
        match = re.search(r'^(\w+)-to-(\w+) map:$', lines[0])
        source_type = match.group(1)
        dest_type = match.group(2)
        sections[source_type] = (dest_type, Section(lines[1:]))
    min_location = None

    for seed_range in seeds:
        current_type = 'seed'
        map = {(seed_range[0], seed_range[0] + seed_range[1]): 0}
        #print('>>>', current_type, apply_map(map, 82))
        while current_type != 'location':
            current_type, section = sections[current_type]
            map = combine_maps(map, section.get_map())
            #print('>>>', current_type, apply_map(map, 82))
            #print(current_type, section.get_map())
        for key, value in map.items():
            min_number = key[0] + value
            if min_location is None or min_location > min_number:
                min_location = min_number
    return min_location

#result = part_1()
result = part_2()
print(result)
