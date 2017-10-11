import sys
from collections import defaultdict
from heapq import *

input = sys.stdin.readline

n, m = (int(i) for i in input().split())

def djik(graph, danger, targ):
  global n
  q = [(0, 0, 1)]
  visited = [0 for i in range(n+1)]
  done = False
  while q:
    succ, splooge, x = heappop(q)
    if x == targ:
      done = True
      print(succ, splooge)
      return
    visited[x] = 1;
    for node in graph[x]:
      if visited[node] == 0:
        heappush(q, (succ + danger[(x, node)], splooge + 1, node))
  print(-1)

danger = defaultdict(lambda: -420)
graph = [[] for i in range(n+1)]

for i in range(m):
  a, b, t = (int(i) for i in input().split())
  if danger[(a, b)] == -420:
    graph[a].append(b)
    graph[b].append(a)
    danger[(a, b)] = t
    danger[(b, a)] = t
  if t == 0 and danger[(a, b)] == 1:
    danger[(a, b)] = 0
    danger[(b, a)] = 0
    
djik(graph, danger, n)