""" Problem: https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3
"""
class K_Goodness_String:

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
    
    def process(self, case, N, K, S):
        cg = 0
        for i in range(1, (N // 2) + 1):
            if S[i - 1] != S[N - i]:
                cg += 1
        res = abs(K - cg)
        print(f"Case #{case}: {res}")

def main():
    s = K_Goodness_String()
    tc = s.rInt()
    for i in range(tc):
        N, K = s.rIntMap()
        S = s.rStr()
        s.process(i + 1, N, K, S)


if __name__=='__main__':
    main()

