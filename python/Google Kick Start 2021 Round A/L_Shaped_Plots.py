""" Problem: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068c509
"""
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
        #       l  r  u  d   (left, right, up, down)
        ps = [[[0, 0, 0, 0] for j in range(C)] for i in range(R)] # prefixSum
        # ps for left and top
        for i in range(R):
            for j in range(C):
                if A[i][j]: # break ps calculation if A[i][i] == 0
                    ps[i][j][0] = A[i][j]
                    ps[i][j][2] = A[i][j]
                    if i > 0 and A[i - 1][j]:
                        ps[i][j][0] += ps[i - 1][j][0]
                    if j > 0 and A[i][j - 1]:
                        ps[i][j][2] += ps[i][j - 1][2]
        # ps for right and bottom
        for i in range(R - 1, -1, -1):
            for j in range(C - 1, -1, -1):
                if A[i][j]: # break ps calculation if A[i][i] == 0
                    ps[i][j][1] = A[i][j]
                    ps[i][j][3] = A[i][j]
                    if i < R - 1 and A[i + 1][j]:
                        ps[i][j][1] += ps[i + 1][j][1]
                    if j < C - 1 and A[i][j + 1]:
                        ps[i][j][3] += ps[i][j + 1][3]

        def count(short, long):
            return max(0, min(long // 2 - 1, short - 1))

        sides = [(0, 2), (0, 3), (1, 2), (1, 3)]
        for i in range(R):
            for j in range(C):
                for side1, side2 in sides:
                    # count shapes that we can get from this crossroad
                    res += count(ps[i][j][side1], ps[i][j][side2])
                    res += count(ps[i][j][side2], ps[i][j][side1])
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

