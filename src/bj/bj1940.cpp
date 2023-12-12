// bj1940 주몽
#include<bits/stdc++.h>
using namespace std;
int N, M, uniq[15001], cnt;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	cin >> N >> M;
	for (int i = 0; i < N; i++) cin >> uniq[i];
	
	if (M > 200000) cout << 0 << "\n";
	else
	{
		for (int i = 0; i < N; i++)
		{
			for (int j = i+1; j < N; j++)
			{
				if (uniq[i] + uniq[j] == M) cnt++;
			}
		}
		cout << cnt << "\n";
	}
} 