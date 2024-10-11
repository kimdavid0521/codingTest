# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 
# 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 
# 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.

# 제한 사항
# 두 수는 1이상 1000000이하의 자연수입니다.
# 입출력 예
# n	m	return
# 3	12	[3, 12]
# 2	5	[1, 10]
        
# import math
# def solution(n, m):
#     answer = []
#     # 최대공약수
#     for i in range(min(n,m), 0, -1): 
#         if n % i == 0 and m % i == 0:
#             answer.append(i)
#             break 
#     # 최소공배수
#     for i in range(max(n, m), n * m + 1):
#         if i % n == 0 and i % m == 0:
#             answer.append(i)
#             break
#     return answer

# print(solution(3,4))

def solution(n, m):
    bigNum = max(n,m)
    smallNum = min(n,m)
    result = []
    yaksu = 0
    beasu = 0
    for i in range(1, bigNum, 1):
        if(n % i == 0 and m % i == 0):
            yaksu = i
    for i in range(smallNum , bigNum * smallNum, 1):
        if(i % smallNum == 0 and i % bigNum == 0):
            beasu = i
            break
    result.append(yaksu)
    result.append(beasu)
    return result

n = 3
m = 12
print(solution(n,m))