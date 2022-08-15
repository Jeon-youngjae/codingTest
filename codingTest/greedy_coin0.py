# 화폐종류, 거스름 돈
n, k = map(int, input().split())

# 리스트 형태로 돈 받기
coins = []

for _ in range(n):
    coins.append(int(input()))
coins.sort(reverse=True)

# 계산대 돈보다 거스름돈이 더 클 경우 거슬러주기
answer = 0
for money in coins:
    if k >= money:
        answer += k // money
        k %= money
        if k <= 0:
            break
print(answer)