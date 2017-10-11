import sys
input = sys.stdin.readline
r, c = (int(i) for i in input().split())
rektrow = [False for i in range(r+1)]
rektcol = [False for i in range(c+1)]

for i in range(r):
  row = list(input())
  for j in range(c):
    if row[j] == 'X':
      rektrow[i+1] = True
      rektcol[j+1] = True
      
q = int(input())
for i in range(q):
  c1, r1 = (int(i) for i in input().split())
  if rektrow[r1] or rektcol[c1]:
    print('Y')
  else:
    print('N')