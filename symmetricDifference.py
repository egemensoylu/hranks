# Enter your code here. Read input from STDIN. Print output to STDOUT


sM = int(input())
M = set([int(x) for x in input().split(' ')])

sN = int(input())
N = set([int(x) for x in input().split(' ')])


[print(x) for x in sorted(list((M.difference(N).union(N.difference(M)))))]
