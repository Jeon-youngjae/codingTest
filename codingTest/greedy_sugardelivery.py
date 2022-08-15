# 입력받을 설탕 양
n = int(input())

# 초기 설탕 봉지 수
count = 0

# 설탕이 0이 될 때까지 반복
while n >= 0:
    if n % 5 == 0: # 5의 배수이면 몫을 봉지에 담는다
        count += n // 5
        break 
    n -= 3 # 3kg씩 봉지에 담는다
    count += 1 # 3kg이 빠질 때마다 1증가 
else: # 계산할 수 없을 때는 -1 출력
    count = -1

print(count)