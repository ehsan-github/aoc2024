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
                words = line.split()
                left.append(int(words[0]))
                right.append(int(words[1]))
            left.sort()
            right.sort()

            res = 0
            for i in range(len(left)):
                res += abs(left[i] - right[i])
            return res    

    ###########################
    # DAY 01 - Second Part
    ###########################

    def _solve_second_part(self) -> int:
        with open("days/day01/input.txt", "r") as f:
            lines = f.read().splitlines()
            left, right = [], []
            for line in lines:
                words = line.split()
                left.append(int(words[0]))
                right.append(int(words[1]))
            left.sort()
            rightCache = {}
            for n in right:
                rightCache[n] = rightCache.get(n, 0) + 1

            res = 0
            for n in left:
                rightVal = rightCache.get(n, 0)
                res += n * rightVal
            return res
