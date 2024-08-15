import sys
input = sys.stdin.readline
n,m  = map(int,input().split())

n_list = [0]+list(map(int,input().split()))

for i in range(1,n+1):
    n_list[i] += n_list[i-1]
for _ in range(m):
    i,j = map(int,input().split())
    print(n_list[j] - n_list[i-1])