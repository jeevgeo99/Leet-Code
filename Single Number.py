class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = {}
        
        for num in nums:
            if num in unique:
                del unique[num]  # Remove if the number appears twice
            else:
                unique[num] = 1  # Add to the dictionary if seen for the first time
        
        # At the end, the dictionary will contain only one element, the single number
        return list(unique.keys())[0]