class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        for index in range(1, len(nums)):
            if nums[index] == nums[index-1]:
                return nums[index-1]