def solution(citations):
    h_index = 0
    for tmp_h in range(len(citations) + 1):
        check_num = 0 # 인용된 논문 갯수
        for citation in citations:
            if tmp_h <= citation:
                check_num += 1
        if tmp_h > check_num:
            h_index = tmp_h - 1
            break
        else:
            h_index = tmp_h

    return h_index
