from collections import defaultdict
import sys


def read_foods():
    return [l.rstrip() for l in sys.stdin.readlines()]


def solve(foods, is_part1):
    allergens_to_possible_ingredient_sets = defaultdict(list)
    ingredient_sets = []
    all_ingredients = set()
    for food in foods:
        food = food.replace('(', '').replace(')', '').replace(',', '')
        ingredients, allergens = [x.split() for x in food.split(' contains ')]
        ingredient_sets.append(ingredients)
        for allergen in allergens:
            allergens_to_possible_ingredient_sets[allergen].append(ingredients)
            for ingredient in ingredients:
                all_ingredients.add(ingredient)

    allergens_to_ingredients = {}
    while allergens_to_possible_ingredient_sets:
        for allergen, ingredients in allergens_to_possible_ingredient_sets.items():
            poss_ingredients = set([poss_i for poss_i in all_ingredients
                                    if all(poss_i in i for i in ingredients)])
            if len(poss_ingredients) == 1:
                ingredient = list(poss_ingredients)[0]
                for a2, possible_ingredient_sets in allergens_to_possible_ingredient_sets.items():
                    allergens_to_possible_ingredient_sets[a2] = [
                        [word for word in row if word != ingredient]
                        for row in possible_ingredient_sets]
                allergens_to_ingredients[allergen] = ingredient
                del allergens_to_possible_ingredient_sets[allergen]
                break

    if is_part1:
        not_allergens = defaultdict(int)
        for ingredients in ingredient_sets:
            for ingredient in ingredients:
                if ingredient not in allergens_to_ingredients.values():
                    not_allergens[ingredient] += 1
        return sum(not_allergens.values())

    res = ''
    for allergen in sorted(allergens_to_ingredients):
        res += f'{allergens_to_ingredients[allergen]},'
    return res[:-1]


if __name__ == '__main__':
    foods = read_foods()
    print(f'Part 1: {solve(foods, True)}')
    print(f'Part 2: {solve(foods, False)}')
