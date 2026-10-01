class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in hashset:
                return True
            hashset.add(num)
        return False


# Notes 
# When checking for an existing element, utilize a set to get immediate access to element values.
# If checking for duplicate values, check for the current value in set, and if it does not exist, populate it into the set.

# Syntax: 
# x = set()
# bool vals: True, False, first letter capitalized

