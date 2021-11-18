import collections
import bisect
class string: 
  def ShortestWay(self, source, target): 
    s_target = set(target)
    pos = collections.defaultdict(list)
    for i, v in enumerate(source): 
      pos[v].append(i)
    if any(key not in pos for key in s_target): return -1 
    
    n = len(target)
    dp = [n] * (n + 1)
    dp[-1] = 0
    for i, v in enumerate(target):
      dp[i] = min(dp[i], dp[i-1] + 1)
      cur = pos[v][0]
      k = i + 1 
      while k < n and pos[target[k]][-1] > cur: 
        u = target[k]
        idx = bisect.bisect(pos[u], cur)
        dp[k] = min(dp[k], dp[i])
        cur = pos[u][idx]
        k += 1 
      #dp[k] = min(dp[k], dp[i] + 1)
      
    return dp[n-1] 
t = string()
print(t.ShortestWay('acder', 'aderacderddee'))
print(t.ShortestWay(source = "xyz", target = "xzyxz"))


