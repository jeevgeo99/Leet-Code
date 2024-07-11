class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindromes
        if x < 0:
            return False
        
        # Convert the integer to a string
        str_x = str(x)
        
        # Reverse the string
        reversed_str_x = str_x[::-1]
        
        # Check if the original string is equal to the reversed string
        return str_x == reversed_str_x

# Creating an instance of the Solution class
solution = Solution()

# Calling the isPalindrome method with different test cases
print(solution.isPalindrome(121))  # Output: True
print(solution.isPalindrome(-121)) # Output: False
print(solution.isPalindrome(10))   # Output: False
