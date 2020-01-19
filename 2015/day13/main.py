import itertools
import re
import sys

def read_input():
    pattern = r'(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+).'
    mood_change = {}
    names = set()
    for line in sys.stdin:
        person, change, amount, neighbour = re.findall(pattern, line)[0]
        amount = -int(amount) if change == 'lose' else int(amount)
        mood_change[(person, neighbour)] = amount
        names.add(person)
    return mood_change, names

def get_mood(mood_change, names):
    max_total_mood = 0
    for p in itertools.permutations(names): # includes reverse order and other duplicate arrangements
        total_mood = 0
        for i, person in enumerate(p):
            neighbour = p[0] if i == len(p) - 1 else p[i+1]
            total_mood += mood_change[(person, neighbour)]
            total_mood += mood_change[(neighbour, person)]
        max_total_mood = max(total_mood, max_total_mood)
    return max_total_mood

mood_change, names = read_input()
print('Part 1:', get_mood(mood_change, names))

names.add('me')
for person, neighbour in itertools.combinations(names, 2):
    if person == 'me' or neighbour == 'me':
        mood_change[(person, neighbour)] = 0
        mood_change[(neighbour, person)] = 0
print('Part 2:', get_mood(mood_change, names))
