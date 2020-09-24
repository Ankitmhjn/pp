def LCS(s, i, m, t, j, n):
    if i==m or j==n:
        return 0
    elif s[i] != t[j]:
        return max(LCS(s, i+1, m, t, j, n), LCS(s, i, m, t, j+1, n))
    else:
        return 1+LCS(s, i+1, m, t, j+1, n)

print(LCS('ankit', 0, 5, 'ankit', 0, 5))