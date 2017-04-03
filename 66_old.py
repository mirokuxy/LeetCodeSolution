class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        L = len(digits)
        carry = 1
        for i in xrange(L-1, -1, -1):
            sum = digits[i] + carry
            carry = sum / 10
            digits[i] = sum % 10
        if carry > 0:
            digits = [carry] + digits
        return digits
        