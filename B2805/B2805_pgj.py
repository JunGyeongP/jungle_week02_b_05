import sys
sys.setrecursionlimit(10**6)

N, M = map(int, sys.stdin.readline().strip().split())
tree = list(map(int, sys.stdin.readline().strip().split()))

start = 1
end = max(tree)


max = 0
while(start <= end):   
    mid = (start + end) // 2
    total= [tree-mid if tree>mid else 0 for tree in tree]
    sum_tree = sum(total)
    if(sum_tree >= M):
        start = mid + 1
        if(sum_tree == M): 
            max = mid
    else:
        end = mid - 1

print(max)