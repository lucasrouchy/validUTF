class Solution:
    def validUtf8(self, data: 'list[int]') -> bool:
        while data:
            for (int i =0; i < len(data); i++):