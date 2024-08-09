# Q: Given a list of nums that are not necessarily distinct, return all distinct subsets.

# T: O(n * 2^n)
# In worst case we wouldn't have any duplicates and we have to create a branch in the decision tree for each el. We wouldn't
# skip any values. So the number of nodes(size of the tree) would be 2^n and for each subset it takes n to build it(in the worst
# case - which is caused by curSet.copy()).

# M: O(n) - the height of the tree
def subsetsWithDuplicates(nums):
    nums.sort()
    subsets, curSet = [], []
    helper(0, nums, curSet, subsets)


def helper(i, nums, curSet, subsets):
    if i >= len(nums):
        subsets.append(curSet.copy())

        return

    # decision to include nums[i]
    curSet.append(nums[i])
    helper(i + 1, nums, curSet, subsets)
    curSet.pop()

    # decision to NOT include nums[i]
    # Note: Remember we wanna avoid duplicate subsets over multiple subtrees not using duplicate numbers for the same subtree.
    # So using 2 twice or more in the same subtree is ok, which is why we're appending the next num in the prev lines.
    # We just don't want the same num to be used again in another subtree(another subtree means after popping from curSet).
    # Note: When we reach duplicate vals, we wanna skip ALL of them when going down to another subtree.
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1

    helper(i + 1, nums, curSet, subsets)