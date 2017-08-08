# 282. Expression Add Operators
# https://leetcode.com/problems/expression-add-operators/description/

# Solution: DFS
#   1)For every position between 2 digits, there are 4 possibilities:
#     no operator; operator +, operator -, operator *
#     Try all of them 
#   2) if using python: eval result string directly to get value,
#      if not using python, eval on the go, special care to operator *.
#   3) special care to digit 0, since 0 can't be starting digit for num except for 0

OPS = ['+', '-', '*']

def constructExpression(num, ops):
  ans = []
  for i in xrange(len(num)):
    ans.append(ops[i])
    ans.append(num[i])

  return ''.join(ans)

def generateOperators(num, target, ops, pos, zero_start, ans):
  if pos == len(num):
    expression = constructExpression(num, ops)
    res = eval(expression)
    if res == target:
      ans.append(expression)
    return

  # don't insert op
  if not zero_start:
    ops[pos] = ''
    generateOperators(num, target, ops, pos+1, False, ans)

  # insert op
  zero_start = num[pos] == '0'
  for op in OPS:
    ops[pos] = op
    generateOperators(num, target, ops, pos+1, zero_start, ans)

  return

class Solution(object):
  def addOperators(self, num, target):
    """
    :type num: str
    :type target: int
    :rtype: List[str]
    """
    if len(num) == 0:
      return []

    ops = [''] * len(num)
    ans = []

    zero_start = num[0] == '0'
    generateOperators(num, target, ops, 1, zero_start, ans)

    return ans

s = Solution()
ans = s.addOperators("123456789", 45)
print(ans)
    