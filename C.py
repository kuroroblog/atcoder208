import copy

# 標準入力を受け付ける。
N, K = map(int, input().split())

A = list(map(int, input().split()))

# 全員に配るお菓子の数を求める。
all_snack_num = K // N
# 全員に均等にお菓子を配った場合に、残るお菓子の数を求める。
amari_snack_num = K - (all_snack_num * N)

# 参考 : https://qiita.com/Kaz_K/items/a3d619b9e670e689b6db
sortedA = copy.copy(A)
# 国民番号をソートする。
sortedA.sort()

# 残りのお菓子を配る際に、最後にお菓子を配る国民番号を取得する。
# amari_snack_numが0の場合もエラーにならない。 ⏩ 1 <= Nのため。
last_user_for_distribute_snack = sortedA[amari_snack_num - 1]

for a in A:
    # 残りのお菓子がある && 最後に残りのお菓子を配る国民番号 >= 国民番号の場合、全員に配るお菓子 + 1となる。
    # そうでない場合、全員に配るお菓子のみとなる。
    if amari_snack_num > 0 and last_user_for_distribute_snack >= a:
        print(all_snack_num + 1)
    else:
        print(all_snack_num)
