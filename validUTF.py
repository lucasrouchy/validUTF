def UTFcheck(nums, s, size):
        for i in range(s+1, s+ size + 1):
            if i >= len(nums) or (nums[i] >> 6) != 0b10: return False
        return True
class Solution:
    #assume everything is correct but have a condition for when its for sure going to be false
   
    def validUtf8( data: 'list[int]') -> bool:
        start = 0
        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110 and UTFcheck(data, start, 3): start +=4
            elif (first >> 4) == 0b1110 and UTFcheck(data, start, 2): start +=3
            elif (first >> 5) == 0b110 and UTFcheck(data, start, 1): start +=2
            elif (first >> 7) == 0: start +=1
            else:
                return False
            return True
    print([197,130,1])
    print(validUtf8([197,130,1]))
    print([235,140,5])
    print(validUtf8([235,140,5]))

    
    
    
