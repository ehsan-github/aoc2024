from scripts.utils import AbstractPuzzleSolver

class PuzzleSolver(AbstractPuzzleSolver):
    ###########################
    # DAY 05 - First Part
    ###########################

    def _solve_first_part(self) -> int:
        rules = set()
        res = 0
        with open("days/day05/input.txt") as f:
            lines = f.read().splitlines()
            reachedOrders = False
            for line in lines:
                if line == "":
                    reachedOrders = True
                    continue
                if not reachedOrders:
                    rules.add(line)
                else:
                    line = [*map(int, line.split(','))]
                    has = True
                    for i in range(len(line)):
                        for j in range(i + 1, len(line)):
                            if f"{line[j]}|{line[i]}" in rules:
                                has = False
                                break
                            pass
                        if not has:
                            break
                    mid = int(line[(len(line) - 1) // 2])
                    res += mid if has else 0
            return res

    ###########################
    # DAY 05 - Second Part
    ###########################
    def fixOrderAndReturnMid(self, line, rules):
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                if f"{line[j]}|{line[i]}" in rules:
                    line[i], line[j] = line[j], line[i]

        mid = int(line[(len(line) - 1) // 2])
        return mid

    def _solve_second_part(self) -> int:
        rules = set()
        res = 0
        with open("days/day05/input.txt") as f:
            lines = f.read().splitlines()
            reachedOrders = False
            for line in lines:
                if line == "":
                    reachedOrders = True
                    continue
                if not reachedOrders:
                    rules.add(line)
                else:
                    line = [*map(int, line.split(','))]
                    has = True
                    for i in range(len(line)):
                        for j in range(i + 1, len(line)):
                            if f"{line[j]}|{line[i]}" in rules:
                                has = False
                                break
                            pass
                    if not has:
                        res += self.fixOrderAndReturnMid(line, rules)
            return res
