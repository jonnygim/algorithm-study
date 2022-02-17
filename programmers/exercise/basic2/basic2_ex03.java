/*
[자연수 뒤집어 배열로 만들기]
> 문제 설명
자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

> 제한 조건
n은 10,000,000,000이하인 자연수입니다.
 */

import java.util.ArrayList;
import java.util.List;

public class basic2_ex03 {
    public static int[] solution(long n) {
        List<Integer> list = new ArrayList<>();

        while (n != 0) {
            list.add((int) (n % 10));
            n /= 10;
        }

        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }


    public int[] solution2(long n) {
        String s = "" + n;
        int[] answer = new int[s.length()];

        for (int i = 0; i < s.length(); i++) {
            answer[i] = s.charAt(s.length() - i - 1) - '0';
        }

        return answer;
    }
}
