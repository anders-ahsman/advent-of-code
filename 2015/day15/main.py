import re
import sys

ingredients = set()
capacity = {}
durability = {}
flavor = {}
texture = {}
calories = {}
pattern = r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (\d+)'
for line in sys.stdin:
    ingredient, cpty, dura, flav, text, cal = re.findall(pattern, line)[0]
    ingredients.add(ingredient)
    capacity[ingredient] = int(cpty)
    durability[ingredient] = int(dura)
    flavor[ingredient] = int(flav)
    texture[ingredient] = int(text)
    calories[ingredient] = int(cal)

ing1, ing2, ing3, ing4 = ingredients
scores = {}
scores500cal = {}
for i in range(100):
    for j in range(100):
        for k in range(100):
            for l in range(100):
                if i + j + k + l == 100:
                    cpty = capacity[ing1] * i + capacity[ing2] * j + capacity[ing3] * k + capacity[ing4] * l
                    dura = durability[ing1] * i + durability[ing2] * j + durability[ing3] * k + durability[ing4] * l
                    flav = flavor[ing1] * i + flavor[ing2] * j + flavor[ing3] * k + flavor[ing4] * l
                    text = texture[ing1] * i + texture[ing2] * j + texture[ing3] * k + texture[ing4] * l
                    score = 0 if any(x < 0 for x in [cpty, dura, flav, text]) else cpty * dura * flav * text
                    scores[(cpty, dura, flav, text)] = score
                    if calories[ing1] * i + calories[ing2] * j + calories[ing3] * k + calories[ing4] * l == 500:
                        scores500cal[(cpty, dura, flav, text)] = score

print('Part 1:', max(scores.values()))
print('Part 2:', max(scores500cal.values()))
