# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.

# 제한 조건
# n은 10,000,000,000이하인 자연수입니다.
# 입출력 예
# n 	return
# 12345	[5,4,3,2,1]

# def solution(n):
#     n = str(n)
#     count = len(n)
#     answer = []
#     for i in range(count):
#         answer.append(int(n[count-1]))
#         count = count -1
#     return answer

def solution(n):
    arr = []
    k = str(n)
    for i in k:
        arr.append(int(i))
    arr.sort(reverse=True)
    return arr

print(solution(12345))