from typing import List
class Soltion:
    def singleNumber(self,nums:List[int]) ->int:

        unique={}

        for num in nums:
            if num in unique:
                del unique[num]
            else:
                unique[num] = 1
        
        return list(unique.keys()) [0]

