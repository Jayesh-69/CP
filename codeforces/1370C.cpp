#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define all(v)   (v.begin()),(v.end())
int primeFactors(ll n)
{

    while (n % 2 == 0)
    {
        n = n / 2;
    }
    int ans = 0;
    // n must be odd at this point.  So we can skip
    // one element (Note i = i +2)
    for (int i = 3; i <= sqrt(n); i = i + 2)
    {
        // While i divides n, print i and divide n
        while (n%i == 0)
        {
            ans++;
            n = n / i;
        }
    }

   // This condition is to handle the case when n
   // is a prime number greater than 2
   if (n > 2)
        ans++;
   return ans;
}
int main(){
    ios_base::sync_with_stdio(0);
    cin.tie();
    cout.tie();

    int t;
    cin>>t;
    while(t--){
        ll n;
        cin>>n;
        if(n==1){
            cout<<"FastestFinger\n";
            continue;
        }
        if(n%2==1){
            cout<<"Ashishgup\n";
            continue;
        }
        if(n==2){
            cout<<"Ashishgup\n";
            continue;
        }
        int twos = 0;
        int odds = primeFactors(n);

        int num = 0;
        while(n%2==0){
            n/=2;
            num++;
        }
        if(odds==0)cout<<"FastestFinger\n";
        else if(num>1)cout<<"Ashishgup\n";
        else if(odds==1) cout<<"FastestFinger\n";
        else cout<<"Ashishgup\n";

    }
}
