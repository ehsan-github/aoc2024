from scripts.utils import AbstractPuzzleSolver


class PuzzleSolver(AbstractPuzzleSolver):
    def isValid(self, nums, with_tolerance=False):
        if len(nums) < 2:
            return 1
        ascend = (nums[1] - nums[0]) > 0
        for i in range(1, len(nums)):
            if (nums[i] == nums[i - 1]) or (((nums[i] - nums[i - 1]) > 0) != ascend) or (abs(nums[i] - nums[i -1]) > 3):
                if with_tolerance:
                    if i == 2:
                        res = self.isValid(nums[1:], False)
                        if res == 1:
                            return 1
                    x = nums.pop(i)
                    res = self.isValid(nums, False)
                    if res == 0:
                        nums[i - 1] = x
                        res = self.isValid(nums, False)
                    return res
                return 0
        return 1

    ###########################
    # DAY 02 - First Part
    ###########################
    def _solve_first_part(self) -> int:
        with open("days/day02/input.txt", "r") as f:
            lines = f.read().splitlines()
            res = 0
            for line in lines:
                nums = list(map(int, line.split()))
                res += self.isValid(nums)
            return res

    ###########################
    # DAY 02 - Second Part
    ###########################

    def _solve_second_part(self) -> int:
        with open("days/day02/input.txt", "r") as f:
            lines = f.read().splitlines()
            res = 0
            for line in lines:
                nums = list(map(int, line.split()))
                res += self.isValid(nums, with_tolerance=True)
            return res
