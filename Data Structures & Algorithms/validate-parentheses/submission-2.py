class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        valid_brackets = {')':'(',
                          '}':'{',
                          ']':'['}
        for letter in s:
            if letter in valid_brackets:
                if stack and stack[-1] == valid_brackets[letter]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(letter)
            
        
        return True if not stack else False

        
        
