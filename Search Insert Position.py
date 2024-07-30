class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Initialize the left and right pointers
        left, right = 0, len(nums) - 1
        
        # Perform binary search
        while left <= right:
            # Find the middle index
            mid = (left + right) // 2
            
            # Print current state
            print("left: {}, right: {}, mid: {}, nums[mid]: {}".format(left, right, mid, nums[mid]))
            
            # Check if the middle element is the target
            if nums[mid] == target:
                print("Target {} found at index {}".format(target, mid))
                return mid
            # If target is greater than the middle element, search the right half
            elif nums[mid] < target:
                left = mid + 1
                print("Target {} greater than nums[mid]. Moving left to {}.".format(target, left))
            # If target is less than the middle element, search the left half
            else:
                right = mid - 1
                print("Target {} less than nums[mid]. Moving right to {}.".format(target, right))
        
        # If the target is not found, return the insertion point
        print("Target {} not found. Insert position is {}.".format(target, left))
        return left

# Examples to test the function
solution = Solution()

# Example 1
print("Example 1:")
print("Input: nums = [1,3,5,6], target = 5")
result = solution.searchInsert([1,3,5,6], 5)
print("Output: {}\n".format(result))

# Example 2
print("Example 2:")
print("Input: nums = [1,3,5,6], target = 2")
result = solution.searchInsert([1,3,5,6], 2)
print("Output: {}\n".format(result))

# Example 3
print("Example 3:")
print("Input: nums = [1,3,5,6], target = 7")
result = solution.searchInsert([1,3,5,6], 7)
print("Output: {}\n".format(result))
