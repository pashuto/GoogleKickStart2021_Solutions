""" Problem: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a882
"""

def process(case, N, S):
    res = [1]
    mx = 1
    for i in range(1, N):
        if ord(S[i - 1]) < ord(S[i]):
            mx += 1
        else:
            mx = 1
        res.append(mx)
    res = " ".join(map(str, res))
    print(f"Case #{case}: {res}")

tcs = int(input())
for tc in range(tcs):
    N = int(input())
    S = input().rstrip()
    process(tc + 1, N, S)