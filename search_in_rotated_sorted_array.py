class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        pivot_point = -1
        # first find the pivot_point
        while left < right:
            if nums[left] > nums[left+1]:
                pivot_point = left
                break
            if nums[right] < nums[right-1]:
                pivot_point = right-1
                break
            left += 1
            right -= 1
        if pivot_point == -1:
            pivot_point = left
        left_nums = nums[:pivot_point+1]
        right_nums = nums[pivot_point+1:]
        if target in left_nums:
            return left_nums.index(target)
        if target in right_nums:
            return len(left_nums) + right_nums.index(target)
        return -1