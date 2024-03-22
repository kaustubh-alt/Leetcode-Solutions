from itertools import permutations
def isValid(s) -> bool:
    stack = []
    for c in s:
      if c == '(':
        stack.append(')')
      elif c == '{':
        stack.append('}')
      elif c == '[':
        stack.append(']')
      elif not stack or stack.pop() != c:
        return False
    return not stack
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        a = n-1
        ansls = []
        numbers = list(range(1,(a*2)+1))
        all_permutations = list(permutations(numbers))
        for i in all_permutations:
            temp = '('
            for j in i:
                if (j//n) < 1:
                    temp+='('
                else:
                    temp+=')'
            temp+=')'
            if isValid(temp):
                ansls.append(temp)
                
        return list(set(ansls))
                
