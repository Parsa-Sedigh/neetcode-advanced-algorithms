"""
Q: Given an array of values, design a data structure that can query the sum of a subarray of the values.
"""
from typing import List


class PrefixSum:
    # T: O(n)
    # M: O(n)
    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0

        for n in nums:
            total += n
            self.prefix.append(total)

    # T: O(1)
    # M: O(1)
    def rangeSum(self, left: int, right: int) -> int:
        preRight = self.prefix[right]

        # if left was given 0, we need to handle the case so that we won't access an out-of-bounds index.
        # Since left is 0, the rangeSum of `right` is the preRight itself. Therefore, we set preLeft to 0 in this case.
        preLeft = self.prefix[left - 1] if left > 0 else 0

        return preRight - preLeft