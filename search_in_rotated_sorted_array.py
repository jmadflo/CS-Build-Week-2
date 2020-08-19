class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left_side = 0
        right_side = len(nums) - 1
        pivot_point = -1
        # first find the pivot_point
        while left_side < right_side:
            if nums[left_side] > nums[left_side+1]:
                pivot_point = left_side
                break
            if nums[right_side] < nums[right_side-1]:
                pivot_point = right_side-1
                break
            left_side += 1
            right_side -= 1
        if pivot_point == -1:
            pivot_point = left_side
        left_nums = nums[:pivot_point+1]
        right_nums = nums[pivot_point+1:]
        if target in left_nums:
            return left_nums.index(target)
        if target in right_nums:
            return len(left_nums) + right_nums.index(target)
        return -1 