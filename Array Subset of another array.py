def isSubset( a1, a2, n, m):

    a1.sort()
    a2.sort()

    i=0
    j=0

    while i<n and j<m:
        if a1[i]==a2[j]:
            i+=1
            j+=1
        elif a2[j]>a1[i]:
            i+=1
        else:
            return "NO"
    return "YES"