""" Problem: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c2c3
    It was super close to Time Limit for the task, so i had to 
    - remove classes
    - use short names 
    - do not use a recursion in UnionFind
    - do not use a rank in UnionFind(which was 4 sec faster for these cases)
    - no wrappers for inputs and skip zero values
"""
from operator import itemgetter

def process(case, N, CV):
    res = 0
    NMAX = 2 * N
    p = [i for i in range(NMAX)]
    
    # UnionFind implementation
    def find(u):
        while u != p[u]:
            p[u] = p[p[u]]
            u = p[u]
        return u
    
    def union(u, v):
        rootU, rootV = find(u), find(v)
        if rootU == rootV:
            return True
        p[rootU] = v
 
    # reverse sort by cost
    for cost, (i, jN) in sorted(CV, key=itemgetter(0), reverse=True):
        if union(i, jN):
            res += cost

    print(f"Case #{case}: {res}", flush=True)

tcs = int(input())
for tc in range(tcs):
    N = int(input())
    for _ in range(N): # skip A
        input()
    CV = []
    # parse and transform in-place to avoid TLE in Python
    for r in range(N):
        for c, v in enumerate(input().split()):
            if v != '0': # skip zero costs
                CV.append((int(v), (r, c + N))) 

    input() # skip R
    input() # skip C
    process(tc + 1, N, CV)

