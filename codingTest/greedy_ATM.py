# 입력받을 사람
n = int(input())

# 줄 서는 사람
person_n = list(map(int, input().split()))

person_n.sort()
result = 0

for i in range(1, n + 1):
    result += sum(person_n[0:i])

print(result)
