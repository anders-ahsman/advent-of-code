import sys

replacements = []
for line in sys.stdin:
    line = line.rstrip()
    if '=>' in line:
        repl_from, repl_to = line.split(' => ')
        replacements.append((repl_from, repl_to))
    else:
        molecule = line

generated = set()
for i in range(len(molecule)):
    for repl_from, repl_to in replacements:
        if molecule[i:i+len(repl_from)] == repl_from:
            generated.add(molecule[:i] + repl_to + molecule[i+len(repl_from):])
print('Part 1:', len(generated))
