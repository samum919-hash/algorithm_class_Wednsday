# 여행 짐 꾸리기 최적 패킹 프로그램
# 0/1 배낭 문제
# 가져갈 수 있는 짐
# 물건번호  물건이름    무게(wt)    만족도(A(i,w))
# 1         노트북      3           12
# 2         카메라      1           10
# 3         책          2           6
# 4         옷          2           7
# 5         충전기      1           4

# 요구사항
# 사용자에게 배낭용량 입력받음
# 선택된 물건의 목록 출력
# 총 만족도 출력
# DP 테이블 방식 구현
# 선택된 물건을 역추적 하는 기능 포함

inf = [[1, "노트북", 3, 12],
       [2, "카메라", 1, 10], 
       [3, "책",    2, 6], 
       [4, "옷",    2, 7],
       [5, "휴대용 충전기", 1, 4]]
    # inf[~][0] = 물건번호  i
    # inf[~][1] = 물건이름  name
    # inf[~][2] = 무게      wt
    # inf[~][3] = 만족도    A(i,w)

n = len(inf)
names = [it[1] for it in inf]
wt = [it[2] for it in inf]
val = [it[3] for it in inf]
    

def packing(max_w, wt, val, n):
    # DP 테이블 A (행: 0..n, 열: 0..W)
    A = [[0] * (max_w + 1) for _ in range(n + 1)]

    # 테이블 채우기 (요청하신 코드 구조 사용)
    for i in range(1, n + 1):
        for w in range(1, max_w + 1):
            if wt[i-1] > w:
                A[i][w] = A[i-1][w]
            else:
                valWith = val[i-1] + A[i-1][w - wt[i-1]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)
                
    total_value = A[n][max_w]
    
    selected_indices = []
    w = max_w

    for i in range(n, 0, -1):
        # 만약 이 행의 값이 위 행과 다르면 i번째 물건이 선택된 것
        if A[i][w] != A[i-1][w]:
            selected_indices.append(i-1)  # items 리스트는 0-based
            w -= wt[i-1]

    # 출력
    print("\n=== 선택 결과 ===")
    if selected_indices:
        selected_indices.reverse()  # 원래 순서대로
        print("선택된 물건:")
        for idx in selected_indices:
            print(f" - {names[idx]} (무게: {wt[idx]}, 만족도: {val[idx]})")
    else:
        print("선택된 물건이 없습니다.")

    print(f"\n총 만족도: {total_value}")
    print(f"배낭에 사용된 무게 합: {sum(wt[i] for i in selected_indices)} / {max_w}")

# test
if __name__ == "__main__":
    max_w = int(input("배낭용량을 정수로 입력 : "))
    packing(max_w, wt, val, n)
