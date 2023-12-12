// bj1213 팰린드롬 만들기 
#include<bits/stdc++.h>
using namespace std;
string name, rtn;
int cnt[200], flag;
char mid;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> name;
	
	for (char a : name) cnt[a]++; // 문자 카운팅 해두기 아스키코드로 
	
	// 알파벳 돌면서 
	// 정답이 여러개인 경우 사전 순으로 출력하라했기에 Z 부터 추가
	for (int i = 'Z'; i >= 'A'; i--) // Z 가 90 이라 90 부터 
	{
		if (cnt[i])
		{
			if (cnt[i] & 1) // 비트 연산자로 홀수 체크 가능 
			{
				// 홀수 이면 mid 값에 저장. flag 로 홀수 카운트(2개 이상일 경우 못 만듬) 
				mid = char(i); // 홀수는 중앙에 넣어야함 
				flag++;
				cnt[i]--; // 짝수로 만들기 
			}
			if (flag == 2) break;
			
			// 붙이기 
			for (int j = 0; j < cnt[i]; j += 2)
			{
				rtn = char(i) + rtn; // 앞에다가 붙이고 
				rtn += char(i); // 뒤에 붙이고  
			}
		}
	}
	if (mid) rtn.insert(rtn.begin() + rtn.size() / 2, mid); // 총 길이에 절반 위치에 mid 넣어줌. 
	if (flag == 2) cout << "I'm Sorry Hansoo\n";
	else cout << rtn << "\n";
}