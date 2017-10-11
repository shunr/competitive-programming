from collections import defaultdict
from collections import Counter

meme = defaultdict(int)
n = int(input())
for x in input().split():
  meme[x] += 1

count = Counter(meme)
c, most = count.most_common(1)[0]
s = 0

for k, v in meme.items():
  if k != c:
    s += v
    
print(s * 2 + 1 if (most > s) else s + most)