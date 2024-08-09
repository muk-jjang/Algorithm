import sys

N = sys.stdin.readline()

n_list = list(N)
n = int(N)

for i in range(1, n+1):
    sum_num = sum((map(int, str(i))))
    sum_num += i

    if sum_num == n :
        print(i)
        break
    if i == n:
        print(0)

'''
반례 한자리가 들어오면 for문이 음수부터 돌게 돼있음, 따라서 n-9*자릿수로 접근하면 안 됨
다만 앞에 조건문을 달아주면 시간복잡도는 더 줄일 수 있을거 같음
'''