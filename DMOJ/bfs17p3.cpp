#include <bits/stdc++.h>

#define SUCC 3030
#define f first
#define s second
#define mp make_pair

using namespace std;

vector<int> graph[SUCC];
pair<int, int> pos[SUCC];
long long range[SUCC];
int m, n, s, kobe;
int furthest = 0;

int bfs(int m) {
  bool v[SUCC] = { 0 };
  for (int i = 1; i <= m; i++) {
    int x, y, r;
    scanf("%i %i %i", &x, &y, &r);
    pos[i].f = x;
    pos[i].s = y;
    range[i] = r;
    if (r == 9001) {
      kobe = i;
    }
    if (y > furthest) {
      furthest = y;
      s = i;
    }
  }
  
  for (int i = 1; i <= m; i++) {
    for (int j = 1; j <= m; j++) {
      if (pow(pos[i].f - pos[j].f, 2) + pow(pos[i].s - pos[j].s, 2) <= (long) pow(range[i], 2) && i != j) {
        graph[i].push_back(j);
      }
    }
  }
  
  deque<pair<int, int>> q;
  q.push_back(mp(s, 0));
  while (q.size() > 0) {
    pair<int, int> x = q.front();
    if (x.f == kobe) {
      return x.s;
    }
    q.pop_front();
    v[x.f] = true;
    for (int i = 0; i < graph[x.f].size(); i++) {
      if (!v[graph[x.f][i]]) {
        q.push_back(mp(graph[x.f][i], x.s + 1));
      }
    }
  }
  return 999999999;
}

int main() {
  scanf("%i %i", &m, &n);
  int home = bfs(m);
  for (int i = 1; i <= m; i ++) {
    graph[i].clear();
  }
  furthest = 0;
  int away = bfs(n);
  if (home == away) {
    printf("SUDDEN DEATH");
  } else if (home < away) {
    printf("We are the champions!");
  } else {
    printf(":'(");
  }
}