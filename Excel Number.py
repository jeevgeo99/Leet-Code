class Solution:
    def titleToNumber(self,columnTitle:str) ->int:
        result =0
        for char in columnTitle:
           current_value= ord(char) - ord('A') + 1
           result = result*26 + current_value
        
        return result
        