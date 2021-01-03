import sys


def read_input():
    rule_lines, messages = [section.split('\n') for section in sys.stdin.read().split('\n\n')]

    def parse_rule(s):
        key, rule = s.split(': ')
        rule = rule[1] if '"' in rule else [[term for term in r.split()] for r in rule.split('|')]
        return (key, rule)
    rules = dict(parse_rule(s) for s in rule_lines)

    return rules, messages


def matches_rules(message, sub_rules):
    if not message or not sub_rules:
        return not message and not sub_rules  # "clean" ending => entire string matched

    rule = rules[sub_rules[0]]
    if type(rule) == str:
        if message[0] in rule:
            return matches_rules(message[1:], sub_rules[1:])
        else:
            return False
    else:
        return any(matches_rules(message, t + sub_rules[1:]) for t in rule) # expand first term


if __name__ == '__main__':
    rules, messages = read_input()
    print(f'Part 1: {sum(matches_rules(m, ["0"]) for m in messages)}')
