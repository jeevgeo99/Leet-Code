class Solution:
    def strStr(self,haystack:str,needle:str)->int:
        haystack_length=len(haystack)
        needle_length=len(needle)

        if needle_length > haystack_length:
            return -1
        
        i=0
        while i< (haystack_length - needle_length+1):
            if haystack[i:i+needle_length] == needle :
                return i
            
            i+=1

        return -1

