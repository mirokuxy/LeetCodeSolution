# 282. Expression Add Operators
# https://leetcode.com/problems/expression-add-operators/description/

OPS = ['+', '-', '*']

def calc(arg1, op, arg2):
  if op == '+':
    return arg1 + arg2
  elif op == '-':
    return arg1 - arg2
  else:
    return arg1 * arg2

def generateExpression(num, target, pos, exp, arg1, op1, arg2, ans):
  #if pos < 3:
  #print(pos, exp, arg1, op1, arg2, ans)
  if pos == len(num):
    if arg2:
      res = calc(arg1, op1, arg2)
    else:
      res = arg1
    if res == target:
      ans.append(exp)
      #print(exp, ans, arg1, op1, arg2)
    return

  for i in xrange(pos, len(num)): # last digit of current int
    temp_arg = int(num[pos:i+1])

    if arg2 != None or arg1 != None:
      for temp_op in OPS:
        new_arg1, new_op1, new_arg2 = arg1, op1, arg2
        if temp_op == '*':
          if arg2 != None:
            new_arg2 = calc(arg2, temp_op, temp_arg)
          else:
            new_arg1 = calc(arg1, temp_op, temp_arg)
        else:
          if arg2 != None:
            new_arg1 = calc(arg1, op1, arg2)
            new_op1 = temp_op
            new_arg2 = temp_arg
          else:
            new_op1 = temp_op
            new_arg2 = temp_arg
        new_exp = exp + temp_op + str(temp_arg)
        generateExpression(num, target, i+1, new_exp, new_arg1, new_op1, new_arg2, ans)
    else: # no arg1
      new_arg1 = temp_arg
      new_exp = str(temp_arg)
      generateExpression(num, target, i+1, new_exp, new_arg1, None, None, ans)

    if temp_arg == 0: break   # avoid futher loop where 0 is starting digit

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

    ans = []
    generateExpression(num, target, 0, "", None, None, None, ans)

    return ans

s = Solution()
ans = s.addOperators("005", 5)
print(ans)

    