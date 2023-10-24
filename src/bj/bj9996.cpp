#include <bits/stdc++.h>
using namespace std;
int n;
string s, ori_s, pre, suf;
int main()
{
    cin >> n;
    cin >> ori_s;
    int pos = ori_s.find('*');
    pre = ori_s.substr(0, pos);
    suf = ori_s.substr(pos + 1); // 하나의 인덱스만 넣으면 끝까지 뽑아냄.

    for (int i = 0; i < n; i++)
    {
        cin >> s;
        if (pre.size() + suf.size() > s.size()) // 최소 pre + suf 길이는 돼야 함
        {
            cout << "NE\n";
        }
        else
        {
            if (pre == s.substr(0, pre.size()) && suf == s.substr(s.size() - suf.size())) cout << "DA\n";
            else cout << "NE\n";
        }
    }



    // 총 N 개의 줄에 걸쳐서 입력으로 주어진 i 번째 파일과 이름이 같으면 DA, 다르면 NE

    return 0;
}
