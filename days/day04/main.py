import re
from scripts.utils import AbstractPuzzleSolver


class PuzzleSolver(AbstractPuzzleSolver):
    ###########################
    # DAY 04 - First Part
    ###########################

    def _solve_first_part(self) -> int:
        with open("days/day04/input.txt") as f:
            lines = f.read().splitlines()
            res = 0
            horizontal = [''] * len(lines)
            diagonal = [''] * (len(lines) + len(lines[0]) + 1)
            diagonalRev = [''] * (len(lines) + len(lines[0]) + 1)
            total_rows = len(lines)
            for rowIdx, line in enumerate(lines):
                res += len(re.findall("XMAS", line))
                res += len(re.findall("SAMX", line))
                for idx, char in enumerate(line):
                    horizontal[idx] += char
                    diagonal[(idx - rowIdx) + total_rows] += char
                    diagonalRev[(idx + rowIdx)] += char
            for line in horizontal:
                res += len(re.findall("XMAS", line))
                res += len(re.findall("SAMX", line))
            for line in diagonal:
                res += len(re.findall("XMAS", line))
                res += len(re.findall("SAMX", line))
            for line in diagonalRev:
                res += len(re.findall("XMAS", line))
                res += len(re.findall("SAMX", line))
            return res

    ###########################
    # DAY 04 - Second Part
    ###########################

    def _solve_second_part(self) -> int:
        with open("days/day04/input.txt") as f:
            lines = f.read().splitlines()
            diagonal = [''] * (len(lines) + len(lines[0]) + 1)
            diagonalRev = [''] * (len(lines) + len(lines[0]) + 1)
            total_rows = len(lines)
            for rowIdx, line in enumerate(lines):
                for idx, char in enumerate(line):
                    # set rowIdx and colIdx instead of A character to check if it has been repeated
                    # both in diagonal and none diagonal matrixes
                    c = char if char != "A" else str(rowIdx * len(line) + idx)
                    diagonal[(idx - rowIdx) + total_rows] += c
                    diagonalRev[(idx + rowIdx)] += c

            diag = []
            diagRev = []
            for line in diagonal:
                diag += re.findall(r"M(\d+)S", line)
                diag += re.findall(r"S(\d+)M", line)

            for line in diagonalRev:
                diagRev += re.findall(r"M(\d+)S", line)
                diagRev += re.findall(r"S(\d+)M", line)

            return len([n for n in diag if n in diagRev])
