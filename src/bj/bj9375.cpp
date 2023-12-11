/*
Bj9375 : 패션왕 신해빈
*/
#include<bits/stdc++.h>
using namespace std;
int tc, n;
string a, b;

int main()
{
	cin >> tc;
	while(tc--)
	{
		map<string, int> _map;
		cin >> n;
		for (int i = 0; i < n; i++)
		{
			cin >> a >> b;
			_map[b]++; // 의상 이름은 필요 없으니 종류만 몇 개인지 파악 
		}
		long long ret = 1;
		for (auto c : _map) // map 다 순회하면서 
		{
			 ret *= ((long long) c.second + 1); // second : value / 종류별 안입는 경우 +1 
		}
		ret--; // 전체 안입는거 제외 
		cout << ret << "\n"; 
	} 
}