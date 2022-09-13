class Solution:
    #assume everything is correct but have a condition for when its for sure going to be false
    def UTFcheck(nums, s, size):
        for i in range(s+1, s+ size + 1):
            if i >= len(nums) or (nums[i] >> 6) != 0b10: return False
        return True
    def validUtf8(self, data: 'list[int]') -> bool:
        start = 0
        
