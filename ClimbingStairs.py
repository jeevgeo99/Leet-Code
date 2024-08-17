class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2

        # Initialize the number of ways to get to the first two steps
        first = 1
        second = 2

        # Calculate the number of ways for each step from 3 to n
        for i in range(3, n + 1):
            third = first + second  # The current step depends on the previous two steps
            first = second  # Move the second step to the first step
            second = third  # Move the third step to the second step

        # The second variable now holds the number of ways to get to the nth step
        return second

# Example usage
solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
print(solution.climbStairs(4))  # Output: 5
