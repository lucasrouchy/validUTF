from collections import deque


class Solution:   
    def validUtf8( data: 'list[int]') -> bool:
        start = 0
        #data a deque for easy poping so that we can go through the list of nums effeciently
        data = deque(data)
        try:
            while data:
                #& means only the overlapping will remain and since 0xFF is 255 in hexadecimal all the 1s in the first num will remain
                byt = data.popleft()&0xFF
                #checks to see if the first bit is one so we know its not a 1 byte character
                if byt&0x80:
                    t = 0
                    #cheecks if the byte is 2 bytes
                    if (byt&0b11100000) == 0b11000000:
                        t = 1
                    #checks if the byte is 3 bytes
                    elif (byt&0b11110000) == 0b11100000:
                        t = 2
                    #checks if the byte is 4 bytes
                    elif (byt&0b11111000) == 0b11110000:
                        t = 3
                    #else return false
                    else:
                        return False
                    # while times is not none so it keeps going through this while loop for the rest of the nums
                    while t:
                        byt = data.popleft()&0xFF
                        #if the next bit is not a 1
                        if (byt&0b11000000) != 0b10000000:
                            return False
                        t -= 1
            return True
        except:
            return False




#         def UTFcheck(nums, s, size):
#         for i in range(s+1, s+ size + 1):
#             if i >= len(nums) or (nums[i] >> 6) != 0b10: return False
#         return True
#         while start < len(data):
#             first = data[start]
#             if (first >> 3) == 0b11110 and UTFcheck(data, start, 3): start +=4
#             elif (first >> 4) == 0b1110 and UTFcheck(data, start, 2): start +=3
#             elif (first >> 5) == 0b110 and UTFcheck(data, start, 1): start +=2
#             elif (first >> 7) == 0: start +=1
#             else:
#                 return False
#             return True
    print([197,130,1])
    print(validUtf8([197,130,1]))
    print([235,140,5])
    print(validUtf8([235,140,5]))
    print([240,162,138,147,145])
    print(validUtf8([240,162,138,147,145]))

    
    
    
