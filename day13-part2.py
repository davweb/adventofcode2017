import re

PATTERN = re.compile("(\d+): (\d+)")

def load(filename):
    firewall = {}

    for line in file(filename):
        result = PATTERN.match(line)
        layer, depth = result.group(1, 2)
        layer = int(layer)
        firewall[layer] = int(depth)

    return firewall

def clear(firewall, delay):
    for depth, range in firewall.items():
        turns = depth + delay
        position = turns % (range * 2 - 2)
        if position == 0:
            return False

    return True

delay = 0

firewall = load('day13-input.txt')
while(not clear(firewall,delay)):
    delay += 1

print delay