
class BIT(object):
  def __init__(self, maxVal):
    self.maxVal = maxVal
    self.tree = [0] * (maxVal+1)  # [0, maxVal]
    self.bitmax = self.getBitmax()
  def initWithArray(self, a): # len(a) >= maxVal
    for i in xrange(1, self.maxVal+1):
      self.tree[i] += a[i-1]
      j = i + (i & -i)
      if j <= self.maxVal:
        self.tree[j] += self.tree[i]
  def getBitmax(self):  # assume maxVal > 0
    bitmax = 1
    val = self.maxVal / 2
    while val:
      bitmax <<= 1
      val /= 2
    return bitmax
  def cumulative(self, idx):
    ans = 0
    while idx > 0:
      ans += self.tree[idx]
      idx -= (idx & -idx)
    return ans
  def single(self, idx):
    ans = self.tree[idx]
    z = idx - (idx & -idx)
    idx -= 1
    while idx > z:
      ans -= self.tree[idx]
      idx -= (idx & -idx)
    return ans
  def update(self, idx, diff):
    while idx <= self.maxVal:
      self.tree[idx] += diff
      idx += (idx & -idx)
  def scale(self, times):
    for i in xrange(self.maxVal+1):
      self.tree[i] *= times
  def findG(self, cum):
    bitmax = self.bitmax
    idx = 0
    while bitmax > 0 and idx < self.maxVal:  # idx <= self.maxVal don't forget
      mid = idx + bitmax
      if mid <= self.maxVal and self.tree[mid] <= cum:
        idx = mid
        cum -= self.tree[mid]
      bitmax >>= 1
    if cum > 0:
      return -1
    else:
      return idx
