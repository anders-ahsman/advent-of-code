import sys
from typing import List, Optional, Set, Tuple

from generic_search import Node, astar, node_to_path


replacements: List[Tuple[str, str]] = []
molecule: str = ''
for line in sys.stdin:
    line = line.rstrip()
    if '=>' in line:
        repl_from, repl_to = line.split(' => ')
        replacements.append((repl_from, repl_to))
    else:
        molecule = line

generated: Set[str] = set()
for i in range(len(molecule)):
    for repl_from, repl_to in replacements:
        if molecule[i:i+len(repl_from)] == repl_from:
            generated.add(molecule[:i] + repl_to + molecule[i+len(repl_from):])
print('Part 1:', len(generated))


# Part 2, reverse search from target molecule to 'e'.
replacements_reversed = [(repl_to, repl_from) for repl_from, repl_to in replacements]

def goal_test(m: str) -> bool:
    return m == 'e'

def successors(m: str) -> List[str]:
    succ: Set[str] = set()
    for i in range(len(m)):
        for repl_from, repl_to in replacements_reversed:
            if m[i:i + len(repl_from)] == repl_from:
                succ.add(m[:i] + repl_to + m[i + len(repl_from):])
    return list(succ)

def heuristic(m: str) -> float:
    return len(m) - len('e') # Not valid admissible heuristic?

# Sometimes gives correct answer in < 1s, other times just keeps running.
# Is this because Python's set is random?
solution: Optional[Node[str]] = astar(molecule, goal_test, successors, heuristic)
if solution is None:
    print('Part 2: *** No solution found!')
else:
    path = node_to_path(solution)
    print('Part 2:', len(path) - 1)
