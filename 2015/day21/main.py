import sys
from copy import copy
from dataclasses import dataclass, field
from itertools import combinations
from typing import List, NamedTuple


class Item(NamedTuple):
    name: str
    cost: int
    damage: int
    armor: int


@dataclass
class Character:
    hitpoints: int
    damage: int = 0
    armor: int = 0
    _items: List[Item] = field(default_factory=list)

    @property
    def items(self) -> List[Item]:
        return self._items

    @items.setter
    def items(self, value: List[Item]):
        self._items = value
        for item in self._items:
            self.armor += item.armor
            self.damage += item.damage

    @property
    def item_cost(self) -> int:
        return sum(i.cost for i in self._items)


weapons: List[Item] = [
    Item('Dagger',      8, 4, 0),
    Item('Shortsword', 10, 5, 0),
    Item('Warhammer',  25, 6, 0),
    Item('Longsword',  40, 7, 0),
    Item('Greataxe',   74, 8, 0),
]
armor: List[Item] = [
    Item('Leather',    13, 0, 1),
    Item('Chainmail',  31, 0, 2),
    Item('Splintmail', 53, 0, 3),
    Item('Bandedmail', 75, 0, 4),
    Item('Platemail', 102, 0, 5)
]
rings: List[Item] = [
    Item('Damage +1',  25, 1, 0),
    Item('Damage +2',  50, 2, 0),
    Item('Damage +3', 100, 3, 0),
    Item('Defense +1', 20, 0, 1),
    Item('Defense +2', 40, 0, 2),
    Item('Defense +3', 80, 0, 3)
]

boss_orig = Character(0)
for line in sys.stdin:
    value = int(line.split(': ')[1])
    if 'Hit Points' in line:
        boss_orig.hitpoints = value
    elif 'Damage' in line:
        boss_orig.damage = value
    elif 'Armor' in line:
        boss_orig.armor = value

players: List[Character] = []
for w in weapons:
    for a in list(combinations(armor, 0)) + list(combinations(armor, 1)):
        for r in list(combinations(rings, 0)) + \
                 list(combinations(rings, 1)) + \
                 list(combinations(rings, 2)):
            items: List[Item] = [w]
            for x in a:
                items.append(x)
            for x in r:
                items.append(x)
            player = Character(100)
            player.items = items
            players.append(player)

winners: List[Character] = []
loosers: List[Character] = []
for player in players:
    boss = copy(boss_orig)
    player_attacking: bool = True
    while player.hitpoints > 0 and boss.hitpoints > 0:
        if player_attacking:
            boss.hitpoints -= max(player.damage - boss.armor, 1)
        else:
            player.hitpoints -= max(boss.damage - player.armor, 1)
        player_attacking = not player_attacking
    if player.hitpoints > 0:
        winners.append(player)
    else:
        loosers.append(player)

print('Part 1:', min(p.item_cost for p in winners))
print('Part 2:', max(p.item_cost for p in loosers))
