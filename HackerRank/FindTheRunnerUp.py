n = int(input())
arr = list(map(int,input().split()))[:n]

m = max(arr)
while max(arr) == m:
    arr.remove(max(arr))

print(max(arr))