#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll WS = 16;
ll one = 1;
ll rotl(ll n, ll d, ll MX = WS) {
    return ((n << d)|(n >> (MX - d)))&((one<<MX) - one);
}

ll rotr(ll n, ll d, ll MX = WS) {
    return (n >> d)|(n << (MX - d))&((one<<MX) - one);
}

ll flip(ll n, ll MX = WS){
    return (((one<<MX)-one)^n);
}

ll wt(ll n, ll MX = WS){
    int cnt = 0;
    while(n){
        cnt += (n&1);
        n>>=1;
    }
    return cnt;
}
ll f(ll x, ll MX = WS){
    return (rotl(x, 1, MX)&rotl(x, 8, MX))^rotl(x, 2, MX);
}
pair<ll, ll> split(ll x, ll MX = WS){
    return make_pair((x>>MX), ((x)%(1<<MX)));
}
ll get(ll a, ll n){
    return (a>>n)&1;
}
ll compose(ll l, ll r, ll MX = WS){
    return r + (l<<MX);
}
ll convert(vector<int> a, ll MX = WS){
    ll ret = 0;
    ll exp = 1;
    for(int i = 0; i< MX; i++){
        ret += exp*a[i];
        exp *= 2;
    }
    return ret;
}
ll convert2(vector<int> a, ll MX = WS){
    vector<int> use;
    for(int i = a.size() -1; i>= 0; i--){
        use.emplace_back(a[i]);
    }
    return convert(use, MX);
}

vector<int> arr(ll a, ll MX = WS){
    vector<int> ret;
    for(int i = 0; i<MX; i++){
        ret.emplace_back(get(a, i));
    }
    return ret;
}
int main(){

    return 0;
}
