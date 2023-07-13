s = set(input().split())
ans = True
n = int(input())
for i in range(n):
    t = set(input().split())
    if (s > t) == False:
        ans = False
        break
print(ans)
