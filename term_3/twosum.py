from typing import Optional


def two_sum(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    seen_values: dict[
        int, int
    ] = {}  # this is for caching values so the algorithm is efficient

    # go through each value in nums
    for index, value in enumerate(nums):
        # check if there is a number that can be added to `value` to equal target
        if target - value in seen_values:
            # if so, return that number and the current number's indexes
            return seen_values[target - value], index

        # if not cache the number as it might be used later
        seen_values[value] = index
