#include <bits/stdc++.h>

using namespace std;

int t, a, b;

bool ok(int res, int d){
	long long sum = res * 1LL * (res + 1) / 2;
	if(sum < d) return false;
	return sum % 2 == d % 2;
}	

int main() {		
	cin >> t;
	for(int tc = 0; tc < t; ++tc){
		cin >> a >> b;
		int d = abs(a - b);
		if(d == 0){ 
			cout << "0\n";
			continue;
		}

		int res = 1;
		while(!ok(res, d)) ++res;
		cout << res << endl;
		
	}
	return 0;
}