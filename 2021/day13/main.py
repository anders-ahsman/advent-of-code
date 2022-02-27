#!/usr/bin/env python3

import sys
from dataclasses import dataclass
from typing import List, Set, Tuple


@dataclass(frozen=True)
class Position:
    x: int
    y: int


@dataclass
class FoldInstruction:
    is_x: bool
    value: int


def read_markings_and_fold_instructions() -> Tuple[List[Position], List[FoldInstruction]]:
    markings: List[Position] = []
    fold_instructions: List[FoldInstruction] = []

    for line in sys.stdin:
        if ',' in line:
            x, y = line.split(',')
            markings.append(Position(
                x=int(x),
                y=int(y)
            ))
        elif 'fold' in line:
            line = line.replace('fold along ', '')
            axis, value = line.split('=')
            fold_instructions.append(FoldInstruction(
                is_x=axis == 'x',
                value=int(value)
            ))

    return markings, fold_instructions


def part1(markings: List[Position], fold_instructions: List[FoldInstruction]) -> int:
    markings = fold(markings, fold_instructions[0])
    return len(markings)


def fold(markings: List[Position], fold_instruction: FoldInstruction) -> List[Position]:
    markings_after_fold: Set[Position] = set()

    if fold_instruction.is_x:
        for marking in markings:
            if marking.x < fold_instruction.value:
                markings_after_fold.add(marking)
            elif marking.x > fold_instruction.value:
                markings_after_fold.add(Position(
                    fold_instruction.value - (marking.x - fold_instruction.value),
                    marking.y
                ))
    else:
        for marking in markings:
            if marking.y < fold_instruction.value:
                markings_after_fold.add(marking)
            elif marking.y > fold_instruction.value:
                markings_after_fold.add(Position(
                    marking.x,
                    fold_instruction.value - (marking.y - fold_instruction.value)
                ))

    return list(markings_after_fold)


if __name__ == '__main__':
    markings, fold_instructions = read_markings_and_fold_instructions()
    print(f'Part 1: {part1(markings, fold_instructions)}')
