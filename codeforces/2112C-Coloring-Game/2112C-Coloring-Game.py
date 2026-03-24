t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    for i in range(n):
        for j in range(i):
            x = max(a[n - 1], 2 * a[i]) - a[i] - a[j]
            l, r = 0, j
            while l < r:
                mid = (l + r) // 2
                if a[mid] <= x:
                    l = mid + 1
                else:
                    r = mid
            ans += j - l
    print(ans)