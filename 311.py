# 311. Sparse Matrix Multiplication
# https://leetcode.com/problems/sparse-matrix-multiplication/description/

# Solution:
#  since matrix is sparse, we can convert matrix to a sequence of rows, 
#   each of which is a sequence of (column-number, value) pairs of the nonzero values in the row.

def compressMatrix(A):
  result = []
  for i in xrange(len(A)):
    l = []
    for j in xrange(len(A[i])):
      if A[i][j] != 0: l.append((j, A[i][j]))
    result.append(l)
  return result

class Solution(object):
  def multiply(self, A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    if len(A) == 0 or len(A[0]) == 0 or len(B[0]) == 0: return [ [] ]

    M, K, N = len(A), len(A[0]), len(B[0])
    A = compressMatrix(A)
    B = compressMatrix(B)

    result = [ [ 0 for n in xrange(N) ] for m in xrange(M) ]

    for m in xrange(M):
      for (k, valA) in A[m]:
        for (n, valB) in B[k]:
          result[m][n] += valA * valB

    return result

        