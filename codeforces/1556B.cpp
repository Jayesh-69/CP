#include <iostream>
#include <algorithm>
using namespace std;
typedef long long int ll;
const int N = 1e5 + 5;
int a[N];
int main()
{
	int t;
	cin >> t;
	while (t--)
	{
		int n;
		int j = 0, o = 0;
		ll ansj = 0, anso = 0, cntj = 0, cnto = 0;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> a[i];
			if (a[i] % 2)
			{
				j++;
				ansj += abs(i - cntj * 2);
				cntj++;
			}
			else
			{
				o++;
				anso += abs(i - cnto * 2);
				cnto++;
			}
		}
		if (abs(j-o) > 1)
			cout << -1 << endl;
		else
			if (j == o)
				cout << min(ansj, anso) << endl;
			else if (j > o)
				cout << ansj << endl;
			else if (o > j)
				cout << anso << endl;
	}
}