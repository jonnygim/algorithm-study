/*
Bj1620 : 나는야 포켓몬 마스터 이다솜
*/
#include<bits/stdc++.h>
using namespace std;
int N, M;
string s;
map<string, int> mp;
map<int, string> mp2;
string a[100004];

int main()
{
	ios_base::sync_with_stdio(false); 
	cin.tie(NULL); cout.tie(NULL);  // 입출력 묶음 해제. 
	cin >> N >> M;
	
	for (int i = 0; i < N; i++)
	{
		cin >> s;
		mp[s] = i + 1;
		mp2[i+1] = s;
		a[i+1] = s;
	}
	
	for (int i = 0; i < M; i++)
	{
		cin >> s;
		if (atoi(s.c_str()) == 0) // s가 문자열이면 0
		{
			cout << mp[s] << "\n";
		}
		else // 숫자이면 그대로 출력 
		{
			//cout << a[atoi(s.c_str())] << "\n";
			cout << mp2[atoi(s.c_str())] << "\n";
		}
	}
}