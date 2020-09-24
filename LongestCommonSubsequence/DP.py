import numpy as np
LCS = np.zeros((7, 7))

def LCSLength(s, m, t, n):
    for i in range(m-1, -1, -1):
        for j in range(n-1, i-1, -1):
            LCS[i, j] = LCS[i+1, j+1]

            if s[i]==t[j]:
                LCS[i, j]+=1

            LCS[i, j] = max(LCS[i, j], LCS[i+1, j], LCS[i, j+1])
    
    return LCS[0, 0]

print(LCSLength('ankit', 5, 'bnkota', 5))