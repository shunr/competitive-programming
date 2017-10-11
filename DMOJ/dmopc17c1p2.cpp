#include <bits/stdc++.h>

typedef long long ll;

using namespace std;

ll sums[123456] = {0};

ll nc2(ll n) {
  return (n)*(n-1)/2;
}

map<ll, ll> histo;

int main() {
  int n, m;
  ll final = 0;
  scanf("%i %i", &n, &m);
  
  for(int i = 1; i <= n; i++) {
    ll a;
    scanf("%ld", &a);
    sums[i] = (sums[i-1] + a) % m;
  }
  
  for(int i = 0; i < n + 1; i++) {
    if (histo.find(sums[i]) == histo.end()) histo[sums[i]] = 0;
    histo[sums[i]]++;
  }
  
  for (map<ll, ll>::iterator i=histo.begin(); i!=histo.end(); i++){ 
    final += nc2(i->second);
  }
  
  printf("%lld", final);
  
  return 0;
}