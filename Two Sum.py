class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Create an empty dictionary to store numbers and their indices

        for i, num in enumerate(nums):  # Go through the list with index and number
            complement = target - num  # Calculate the complement (the number we need)

            if complement in num_map:  # Check if the complement is already in the dictionary
                return [num_map[complement], i]  # If it is, return the indices

            num_map[num] = i  # If it's not, add the current number and its index to the dictionary

        return []  # This line is just a fallback and usually won't be reached because there's always one solution

# Example usage:
nums1 = [2, 7, 11, 15]
target1 = 9
solution = Solution()
print(solution.twoSum(nums1, target1))  # Output: [0, 1]

nums2 = [3, 2, 4]
target2 = 6
print(solution.twoSum(nums2, target2))  # Output: [1, 2]

nums3 = [3, 3]
target3 = 6
print(solution.twoSum(nums3, target3))  # Output: [0, 1]
