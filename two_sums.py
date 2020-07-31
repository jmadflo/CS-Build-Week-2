class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        storage = {}
        current = 0
        for index, value in enumerate(nums):
            if target - value in storage:
                return [storage[target - value], index]
            storage[value] = index