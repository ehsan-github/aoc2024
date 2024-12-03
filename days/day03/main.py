from scripts.utils import AbstractPuzzleSolver
import re


class PuzzleSolver(AbstractPuzzleSolver):
    ###########################
    # DAY 03 - First Part
    ###########################

    def _solve_first_part(self) -> int:
        with open("days/day03/input.txt") as f:
            lines = f.read()
            return sum(int(x) * int(y) for x, y in re.findall('mul\((\d+),(\d+)\)', lines))

    ###########################
    # DAY 03 - Second Part
    ###########################

    def _solve_second_part(self) -> int:
        with open("days/day03/input.txt") as f:
            lines = f.read()
            allfinds = re.findall('mul\((\d+),(\d+)\)|(do\(\)|don\'t\(\))',lines)

            res = 0
            do = True
            for x, y, z in allfinds:
                if x == '':
                    do = z == 'do()'
                    continue
                if do:
                    res += int(x) * int(y)
            return res
