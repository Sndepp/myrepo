print("SandeepCC");






"""
def reverse_while_loop(s):
    s1 = ''
    length = len(s) - 1
    while length >= 0:
        s1 = s1 + s[length]
        length = length - 1
    return s1

s2=reverse_while_loop('Sandeep');
print (s2);
"""

class Solution(object):
   def fizzBuzz(self, n):
      """
      :type n: int
      :rtype: List[str]
      """
      result = []
      for i in range(1,n+1):
         if i% 3== 0 and i%5==0:
            result.append("FizzBuzz")
         elif i %3==0:
            result.append("Fizz")
         elif i% 5 == 0:
            result.append("Buzz")
         else:
            result.append(str(i))
      return result
ob1 = Solution()
print(ob1.fizzBuzz(30))
