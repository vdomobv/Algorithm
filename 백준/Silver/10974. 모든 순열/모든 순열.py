from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input())

for i in permutations([j for j in range(1, n+1)], n):
    print(" ".join(list(map(str, i))))