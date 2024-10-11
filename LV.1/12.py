# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# 제한 사항
# n은 0 이상 3000이하인 정수입니다.
# 입출력 예
# n	return
# 12	28
# 5	6
# 입출력 예 설명
# 입출력 예 #1
# 12의 약수는 1, 2, 3, 4, 6, 12입니다. 이를 모두 더하면 28입니다.

# 입출력 예 #2
# 5의 약수는 1, 5입니다. 이를 모두 더하면 6입니다.

# def solution(n):
#     divisors_sum = 0
#     for i in range(1, n + 1):
#         if n % i == 0:
#             divisors_sum += i
#     return divisors_sum

def solution(n):
    result = 0
    for i in range(1,n+1): #이렇게 range를 지정해줄때 1부터 n까지라고 지정해줘야함 아니면 i는 0부터 시작해버려서 약수를 구할때 0이들어가버려서 에러가남
        if(n % i == 0):
            result = result + i
    return result

print(solution(5))