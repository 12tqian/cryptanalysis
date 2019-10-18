#pragma comment(linker, "/stack:200000000")
//#pragma GCC optimize("Ofast")
//#pragma GCC target("sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,tune=native")
#pragma GCC optimize ("O3")
#pragma GCC target ("sse4")
#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll MX = 20;
ll one = 1;
string pad(string s){
    while((s).size()< MX){
        s = '0' + s;
    }
    return s;
}
string bin(long long n){ //long long to binary string
    string result;
    do result.push_back( '0' + (n & 1) );
    while (n >>= 1);

    reverse( result.begin(), result.end() );
    return pad(result);
}

ll rotl(ll n, ll d) {
    return ((n << d)|(n >> (MX - d)))&((one<<MX) - one);
}

ll rotr(ll n, ll d) {
    return (n >> d)|(n << (MX - d))&((one<<MX) - one);
}

ll flip(ll n){
    return (((one<<MX)-one)^n);
}

ll wt(ll n){
    int cnt = 0;
    while(n){
        cnt += (n&1);
        n>>=1;
    }
    return cnt;
}
ll g(ll n){
    ll val = (n| (rotl(n, 1)&flip(rotr(n, 1))));
    return val;
}
const int MAX = 1e5  + 5;
int good[MAX];
int main(){
    for(ll i = 0; i<(one<<MX); i++){
        int w = wt(i);
        if(w == 0 || w == MX) continue;
        if(1<= w && w<MX/2 && wt(g(i)) == w + 1){
            good[w] = 1;
        }
        if(MX/2<= w&& w<MX && wt(g(i)) == w ){
            good[w] = 1;
            if(w == 11) cout << bin(g(i)) << " " << w << endl;
        }
    }
    cout << bin(100) << endl;
    for(int i = 1; i<MX; i++){
        if(good[i] == 0) cout << i << endl;
    }
    return 0;
}
