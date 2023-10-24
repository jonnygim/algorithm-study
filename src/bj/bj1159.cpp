#include <bits/stdc++.h>
using namespace std;
int n, cnt[26];
string s, ret;
int main() {
    cin >> n; // 선수의 수
    for (int i = 0; i < n; i++)
    {
        cin >> s; // 선수의 성이 주어짐;
        cnt[s[0] - 'a']++; // 성의 첫글자를 a == 97 을 빼서 배열에 ++ 함.  a 이면 0
    }
    // 알파벳이 26개 이고 선수 5명 뽑겠다고 했으니
    for (int i = 0; i < 26; i++) if (cnt[i] >= 5) ret += (i + 'a');
    if (ret.size()) cout << ret << "\n";
    else cout << "PREDAJA" << "\n";

    return 0;
}
