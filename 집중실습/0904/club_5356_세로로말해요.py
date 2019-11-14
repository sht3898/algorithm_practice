import sys; sys.stdin = open('5356_input.txt', 'r')
import pprint

for TC in range(1, int(input())+1):
    arr = [list(input()) for _ in range(5)]
    result = ''
    MAX = 0
    pprint.pprint(arr)
    print(arr[1][5])
    for i in range(5):
        for j in range(len(arr[i])):
            MAX = max(0, len(arr[i]))
    for j in range(MAX):
        for i in range(5):
            try:
                result += arr[i][j]
            except Exception as ex:
                print(ex)
    print(result)