# 482. License Key Formatting
# https://leetcode.com/problems/license-key-formatting/#/description

# Solution:
#  calc and append on the fly

# Notes:
# 1) '1'.upper() -> '1' is valid use

class Solution(object):
  def licenseKeyFormatting(self, S, K):
    """
    :type S: str
    :type K: int
    :rtype: str
    """

    raw_s = ''.join(S.split('-'))
    tot_len = len(raw_s)

    ans_l = []

    for i in xrange(tot_len):
      if i != 0 and (tot_len - i) % K == 0:
        ans_l.append('-')
      ans_l.append(raw_s[i].upper())

    return ''.join(ans_l)

def main():
  S = raw_input().strip()
  K = int(raw_input().strip())
  print Solution().licenseKeyFormatting(S,K)

#main()
