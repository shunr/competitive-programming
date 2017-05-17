from sys import stdin

moves = {(7, 3): [(8, 5), (6, 1), (5, 2), (8, 1), (6, 5), (5, 4)], (4, 7): [(6, 8), (3, 5), (2, 6), (5, 5), (6, 6), (2, 8)], (1, 3): [(2, 5), (3, 4), (2, 1), (3, 2)], (6, 6): [(7, 8), (8, 7), (5, 4), (4, 5), (7, 4), (8, 5), (5, 8), (4, 7)], (5, 6): [(6, 8), (7, 7), (4, 4), (3, 5), (6, 4), (7, 5), (4, 8), (3, 7)], (2, 8): [(1, 6), (3, 6), (4, 7)], (7, 8): [(6, 6), (5, 7), (8, 6)], (7, 7): [(6, 5), (5, 6), (8, 5), (5, 8)], (2, 1): [(3, 3), (4, 2), (1, 3)], (6, 2): [(7, 4), (8, 3), (4, 1), (8, 1), (5, 4), (4, 3)], (1, 6): [(2, 8), (3, 7), (2, 4), (3, 5)], (5, 1): [(6, 3), (7, 2), (4, 3), (3, 2)], (3, 7): [(5, 8), (2, 5), (1, 6), (4, 5), (5, 6), (1, 8)], (2, 5): [(3, 7), (4, 6), (1, 3), (3, 3), (4, 4), (1, 7)], (8, 5): [(7, 3), (6, 4), (7, 7), (6, 6)], (5, 8): [(4, 6), (3, 7), (6, 6), (7, 7)], (1, 2): [(2, 4), (3, 3), (3, 1)], (7, 4): [(8, 6), (6, 2), (5, 3), (8, 2), (6, 6), (5, 5)], (3, 1): [(4, 3), (5, 2), (2, 3), (1, 2)], (6, 7): [(8, 8), (5, 5), (4, 6), (7, 5), (8, 6), (4, 8)], (5, 5): [(6, 7), (7, 6), (4, 3), (3, 4), (6, 3), (7, 4), (4, 7), (3, 6)], (8, 1): [(7, 3), (6, 2)], (7, 6): [(8, 8), (6, 4), (5, 5), (8, 4), (6, 8), (5, 7)], (4, 8): [(3, 6), (2, 7), (5, 6), (6, 7)], (4, 4): [(5, 6), (6, 5), (3, 2), (2, 3), (5, 2), (6, 3), (3, 6), (2, 5)], (6, 3): [(7, 5), (8, 4), (5, 1), (4, 2), (7, 1), (8, 2), (5, 5), (4, 4)], (1, 5): [(2, 7), (3, 6), (2, 3), (3, 4)], (3, 3): [(4, 5), (5, 4), (2, 1), (1, 2), (4, 1), (5, 2), (2, 5), (1, 4)], (7, 2): [(8, 4), (5, 1), (6, 4), (5, 3)], (3, 6): [(4, 8), (5, 7), (2, 4), (1, 5), (4, 4), (5, 5), (2, 8), (1, 7)], (2, 2): [(3, 4), (4, 3), (4, 1), (1, 4)], (8, 6): [(7, 4), (6, 5), (7, 8), (6, 7)], (3, 5): [(4, 7), (5, 6), (2, 3), (1, 4), (4, 3), (5, 4), (2, 7), (1, 6)], (4, 1): [(5, 3), (6, 2), (3, 3), (2, 2)], (1, 1): [(2, 3), (3, 2)], (6, 4): [(7, 6), (8, 5), (5, 2), (4, 3), (7, 2), (8, 3), (5, 6), (4, 5)], (3, 2): [(4, 4), (5, 3), (1, 1), (5, 1), (2, 4), (1, 3)], (2, 6): [(3, 8), (4, 7), (1, 4), (3, 4), (4, 5), (1, 8)], (8, 2): [(6, 1), (7, 4), (6, 3)], (7, 1): [(8, 3), (6, 3), (5, 2)], (4, 5): [(5, 7), (6, 6), (3, 3), (2, 4), (5, 3), (6, 4), (3, 7), (2, 6)], (1, 4): [(2, 6), (3, 5), (2, 2), (3, 3)], (7, 5): [(8, 7), (6, 3), (5, 4), (8, 3), (6, 7), (5, 6)], (2, 3): [(3, 5), (4, 4), (1, 1), (3, 1), (4, 2), (1, 5)], (8, 7): [(7, 5), (6, 6), (6, 8)], (6, 8): [(5, 6), (4, 7), (7, 6), (8, 7)], (5, 4): [(6, 6), (7, 5), (4, 2), (3, 3), (6, 2), (7, 3), (4, 6), (3, 5)], (4, 2): [(5, 4), (6, 3), (2, 1), (6, 1), (3, 4), (2, 3)], (6, 5): [(7, 7), (8, 6), (5, 3), (4, 4), (7, 3), (8, 4), (5, 7), (4, 6)], (5, 3): [(6, 5), (7, 4), (4, 1), (3, 2), (6, 1), (7, 2), (4, 5), (3, 4)], (2, 7): [(4, 8), (1, 5), (3, 5), (4, 6)], (8, 3): [(7, 1), (6, 2), (7, 5), (6, 4)], (4, 6): [(5, 8), (6, 7), (3, 4), (2, 5), (5, 4), (6, 5), (3, 8), (2, 7)], (5, 2): [(6, 4), (7, 3), (3, 1), (7, 1), (4, 4), (3, 3)], (6, 1): [(7, 3), (8, 2), (5, 3), (4, 2)], (5, 7): [(7, 8), (4, 5), (3, 6), (6, 5), (7, 6), (3, 8)], (3, 8): [(2, 6), (1, 7), (4, 6), (5, 7)], (1, 8): [(2, 6), (3, 7)], (8, 8): [(7, 6), (6, 7)], (4, 3): [(5, 5), (6, 4), (3, 1), (2, 2), (5, 1), (6, 2), (3, 5), (2, 4)], (1, 7): [(3, 8), (2, 5), (3, 6)], (3, 4): [(4, 6), (5, 5), (2, 2), (1, 3), (4, 2), (5, 3), (2, 6), (1, 5)], (2, 4): [(3, 6), (4, 5), (1, 2), (3, 2), (4, 3), (1, 6)], (8, 4): [(7, 2), (6, 3), (7, 6), (6, 5)]}


start = tuple(int(_) for _ in stdin.readline().strip().split())
end = tuple(int(_) for _ in stdin.readline().strip().split())
q = [(start, 0)]
v = [start]
done = False

while q and not done:
  path = q[0]
  if q[0][0] == end:
      print(0)
      done = True
      break
  for g in moves[path[0]]:
    if g == end:
      print(path[1] + 1)
      done = True
      break
    if g not in v:
      q.append((g, path[1] + 1))
      v.append(g)
  del q[0]