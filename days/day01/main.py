from scripts.utils import AbstractPuzzleSolver



class PuzzleSolver(AbstractPuzzleSolver):
    ###########################
    # DAY 01 - First Part
    ###########################

    def _solve_first_part(self) -> int:
        with open("days/day01/input.txt", "r") as f:
            lines = f.read().splitlines()

            left, right = [], []
            for line in lines:
                l, r = line.split()
                left.append(int(l))
                right.append(int(r))
            left.sort()
            right.sort()
            return sum(abs(l - r) for l, r in zip(left, right))

    ###########################
    # DAY 01 - Second Part
    ###########################

    def _solve_second_part(self) -> int:
        with open("days/day01/input.txt", "r") as f:
            lines = f.read().splitlines()
            left, rightCache = [], {}
            for line in lines:
                l, r = line.split()
                left.append(l)
                rightCache[r] = rightCache.get(r, 0) + 1
            return sum(int(n) * rightCache.get(n, 0) for n in left)
