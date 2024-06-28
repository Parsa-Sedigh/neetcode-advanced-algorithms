# Q: Find a non-empty subarray with the largest sum. Return the largest sum.

# T: O(n^2)
# M: O(1)
def bruteForce(nums):
    # We can't have an empty subarr, so we initialize maxSum as the first el. If we COULD have an empty subarr, we would
    # initialize this to 0, because of the cases where all of the elements are negative or the first one is negative.
    # Note: We could also set this to -Infinity(very small number) because we're trying to find the MAX.
    # Note: We're assuming that nums is non empty, otherwise since our goal is to return the sum of a non-empty subarr,
    # here, we would immediately return.
    maxSum = nums[0]

    # i and j specify the current subarr.
    for i in range(len(nums)):
        curSum = 0

        for j in range(i, len(nums)):
            curSum += nums[j]

            # We need to do the comparison here, not at the end of the second loop, because AT ANY POINT, the curSum could get
            # larger than the maxSum.
            maxSum = max(maxSum, curSum)

    return maxSum

# kadanes algo:
# T: O(n)
def kadanes(nums):
    maxSum = nums[0]
    curSum = 0

    for n in nums:
        # Before we add n to the curSum, we wanna make sure our curSum isn't negative. Because we have a choice: We don't have to
        # include any values that came before n and we would definitely not want to do that if the prev curSum was negative.
        # Because that's never going to increase our maxSum. So with this line of code, we're ensuring that our curSum is never
        # negative.
        # Note: If curSum is negative, we know nothing that came before is gonna help us. Because we need to have a contiguous subarr.
        curSum = max(curSum, 0)

        # after this line, the curSum could become negative, that's why we have the prev line check.
        curSum += n
        maxSum = max(maxSum, curSum)

    return maxSum

# Return the left and right index of the max subarr sum, assuming there's exactly one result(no ties).
# Sliding window variation of kadane's algo(it's based on two-pointers)
# T: O(n)
# M: O(1)

# Note: The left pointer should never cross the right pointer.
def slidingWindow(nums):
    maxSum = nums[0]
    curSum = 0

    # Positions of the window with max sum
    maxL, maxR = 0, 0
    L = 0

    for R in range(len(nums)):
        if curSum < 0:
            curSum = 0
            L = R

        curSum += nums[R]

        if curSum > maxSum:
            maxSum = curSum
            maxL, maxR = L, R

    return [maxL, maxR]