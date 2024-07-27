class Solution(object):
    def longestCommonPrefix(self,strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        prefix=strs[0]


        for string in strs[1:]:
            while string[:len(prefix)] !=prefix :
                prefix=prefix[:-1]

                if not prefix:
                    return ""
                
        
        return prefix
    
sol = Solution()
strs1 = ["flower", "flow", "flight"]
result1 = sol.longestCommonPrefix(strs1)
print("Example 1:")
print("Input: strs =", strs1)
print("Output:", result1)  # Output should be "fl"

# Example 2
strs2 = ["dog", "racecar", "car"]
result2 = sol.longestCommonPrefix(strs2)
print("Example 2:")
print("Input: strs =", strs2)
print("Output:", result2)     