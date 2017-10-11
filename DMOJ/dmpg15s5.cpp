#include <bits/stdc++.h>
#include <stdlib.h> 
#define MAX 10001

bool board[MAX][MAX];
bool row[MAX] = {0};;

int main() {
  memset(board, 0, MAX*MAX*sizeof board[0][0]);
  int n, m;
  int wew = 0;
  scanf("%i %i", &n, &m);
  for (int i = 0; i < m; i++) {
    int x, y, w, h;
    scanf("%i %i %i %i", &x, &y, &w, &h);
    board[x][y] ^= 1;
    board[x+w][y] ^= 1;
    board[x][y+h] ^= 1;
    board[x+w][y+h] ^= 1;
  }
  for (int i = 0; i < n; i++) {
    bool good = 0;
      for (int j = 0; j < n; j++) {
        bool x = board[i][j];
        row[j] ^= x;
        good ^= row[j];
        wew += good;
      }
  }
  printf("%i", wew);
}