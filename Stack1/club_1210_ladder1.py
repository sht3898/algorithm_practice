import sys; sys.stdin = open('1210_input.txt', 'r')

for _ in range(1, 11):
    TC = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    visit = [[0] * 100 for _ in range(100)]
