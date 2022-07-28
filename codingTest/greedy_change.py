n = int(input()) 

count = 0 # 동전 숫자 세기

change = 1000 - n # 잔돈을 받기 위한 변수

coin_list = [500, 100, 50, 10, 5, 1] # 갖고있는 엔화 동전

# 엔화 동전 리스트에서 동전을 꺼내고 몫은 동전의 숫자를 세는데 사용되고 동전으로 나눈 나머지를 통해 잔돈 파악
for coin in coin_list:
    count += change // coin
    change %= coin

print(count)