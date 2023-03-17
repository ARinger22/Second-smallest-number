class Solution:
    def secondSmallest(self, S, D):
        s = S
        st = ""
        if(S >= 9*D or D == 1 or S == 0):
            return -1;
        d = D
        S -= 1
        for i in range(d-1):
            if(S > 9 and D > 1):
                S -= 9
                st += str(9)
                D -= 1
            else:
                st += str(S)
                S = 0
                
        st += str(S+1)
        fin = (st[::-1])
        ans = int(fin)
        new = 10**((s//9)-1)
        if(s%9 == 0 and new > 1): new /= 10
        if(new <= 1): ans += 9
        else: ans += new*9
        return int(ans) 