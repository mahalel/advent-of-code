from operator import mul
from functools import reduce

def get_ways_to_win(races):
    ways_rnd = {}
    for idx, race in enumerate(races):
        cnt = 0
        time, record = race
        for hold in range(1,time):
            if (time - hold) * hold > record:
                cnt += 1
        ways_rnd[idx] = cnt
    return reduce(mul, ways_rnd.values()) 

def main(input):
    with open(input, "r") as f:
        time, distance = iter(f.read().splitlines())
        races_p1 = list(zip([int(x) for x in time.split()[1:]], [int(x) for x in distance.split()[1:]]))
        races_p2 = ((int(''.join(time.split()[1:])), int(''.join(distance.split()[1:]))),)
    return get_ways_to_win(races_p1), get_ways_to_win(races_p2)
 
print(main("./input"))
