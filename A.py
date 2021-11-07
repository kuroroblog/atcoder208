# 標準入力を受け付ける。
A, B = map(int, input().split())

# A回サイコロを振って得られる、最小値、最大値を求める。
min_val = A
max_val = A * 6

# min_val <= B, B <= max_valの場合、`Yes`, そうでなければ`No`を出力する。
if min_val <= B and B <= max_val:
    print('Yes')
else:
    print('No')
