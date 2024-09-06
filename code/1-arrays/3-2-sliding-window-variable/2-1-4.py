"""
Find length of minimum size subarray where the sum is greater than or equal to the target. Assume all values are positive.
"""
def long(nums, target):
    # You can call total, currSum as well
    L, total = 0

    # Since we're trying to minimize the length, by setting it to a really big value, when we run min(), we will end up reducing it.
    # You can also initialize length to be the length of the `input array + 1`, that's also gonna be a good default value.
    length = float("inf")

    for R in range(len(nums)):
        total += nums[R]

        while total >= target:
            length = min(R - L + 1, length)
            total -= nums[L]
            L += 1

    return 0 if length == float("inf") else length
