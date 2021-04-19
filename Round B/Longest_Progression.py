""" Problem: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000435a5b/000000000077a3a5
"""

def calc(D, N):
    res = 0
    i = j = 0
    while i < N:
        i = j
        while j < N and D[i] == D[j]:
            j += 1
        res = max(res, j - i + 1) # D = []: 1 element
        if j < N: # D = [1, 1]: 1 = 2 elements | 1 1 = 3 elements
            res = max(res, j - i + 2)
        if j < N - 1 and 2 * D[i] == D[j] + D[j + 1]:
            second = j + 2 # second progression part
            while second < N and D[second] == D[i]:
                second += 1
            res = max(res, second - i + 1)
    return res

def process(case, N, A):
    D = [A[i] - A[i - 1] for i in range(1, N)]
    res = max(calc(D, N - 1), calc(list(reversed(D)), N - 1))
    print(f"Case #{case}: {res}")

tcs = int(input())
for tc in range(tcs):
    N = int(input())
    A = list(map(int, input().split()))
    process(tc + 1, N, A)