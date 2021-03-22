""" Problem: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509
"""
import heapq

class Solution:

    def trim(self):
        return input()

    def rInt(self):
        return(int(self.trim()))
    
    def rStr(self):
        return(str(self.trim()))

    def rCharList(self):
        s = self.trim()
        return(list(s[:len(s) - 1]))

    def rIntMap(self):
        return(map(int,self.trim().split()))

    def rIntList(self):
        return(list(self.rIntMap()))
    
    def rStrList(self):
        return(list(map(str,self.trim().split())))
    
    def process(self, case, R, C, A):
        res = 0
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        heap = []
        for i in range(R):
            for j in range(C):
                heap.append((-A[i][j], i, j))
        heapq.heapify(heap)
        while heap:
            v, i, j = heapq.heappop(heap)
            v = A[i][j]
            for dx, dy in dir:
                x, y = i + dx, j + dy
                if (0 <= x < R) and (0 <= y < C):
                    if v - A[x][y] > 1:
                        res += v - 1 - A[x][y]
                        A[x][y] = v - 1
                        heapq.heappush(heap, (-A[x][y], x, y))

        print(f"Case #{case}: {res}")

def main():
    s = Solution()
    tc = s.rInt()
    for i in range(tc):
        R, C = s.rIntMap()
        A = [s.rIntList() for _ in range(R)]
        s.process(i + 1, R, C, A)


if __name__=='__main__':
    main()

