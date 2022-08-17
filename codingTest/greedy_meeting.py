import sys
input = sys.stdin.readline

# 미팅 수
n = int(input())

# 미팅 리스트
meeting = []

# 미팅 수 초기값
count = 0

# 미팅 시작, 종료 시간 입력받고 리스트에 추가
for _ in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))

# 종료 시간으로 오름차순 정렬 후 시작 시간으로 오름차순 정렬
meeting = sorted(meeting, key=lambda x: (x[1], x[0]))

# 종료 시간 초기값
meeting_end = 0

# 각 meet 지정
for meet in meeting:
    start = meet[0]
    end = meet[1]
    # 미팅 시작 시간이 종료 시간보다 같거나 크면 미팅 수 증가
    if start >= meeting_end:
        count += 1
        # 미팅 종료 시간을 다시 end로 정의
        meeting_end = end

# 미팅 수 출력
print(count)