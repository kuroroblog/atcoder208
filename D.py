# 標準入力を受け付ける。
N, M = map(int, input().split())

# 都市間の移動ができない、移動時間を表す
INF = 1000000000000000000

# 都市間の移動時間情報を格納する。
time = []
for i in range(N):
    time.append([INF] * N)
    time[i][i] = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    # 配列の都合上、-1idxを行う。
    A -= 1
    B -= 1
    time[A][B] = C

ans = 0
for k in range(N):
    for i in range(N):
        for j in range(N):
            # Start ⏩ Goal or Start ⏩ 都市x ⏩ Goalの最小移動時間を求める。
            time[i][j] = min(time[i][j], time[i][k] + time[k][j])
            # 都市間の移動ができない、移動時間の場合、答えに含まない。
            if time[i][j] == INF:
                continue
            ans += time[i][j]

print(ans)
