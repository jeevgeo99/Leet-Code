class Solution(object):
    def lengthOfLastWord(self,s):
         """
        :type s: str
        :rtype: int
        """
         trimmed_s=s.strip()
         words=trimmed_s.split()
         last_word=words[-1]
         return len(last_word)

sol = Solution()

# Test the method with example strings and print the result
print(sol.lengthOfLastWord("Hello World"))                # Output: 5
print(sol.lengthOfLastWord("   fly me   to   the moon  ")) # Output: 4
print(sol.lengthOfLastWord("luffy is still joyboy"))