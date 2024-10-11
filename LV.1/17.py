# 정수를 저장한 배열, arr 에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요. 
# 단, 리턴하려는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요. 예를들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10]면 [-1]을 리턴 합니다.

# 제한 조건
# arr은 길이 1 이상인 배열입니다.
# 인덱스 i, j에 대해 i ≠ j이면 arr[i] ≠ arr[j] 입니다.
# 입출력 예
# arr	return
# [4,3,2,1]	[4,3,2]
# [10]	[-1]

# 풀이에서는 min() 함수를 사용하여서 배열의 가장 작은 값을 추출하였다
# 그 후 remove() 함수를 사용하여서 배열에서 그 값을 지워주었다

# def solution(arr):
#     length = len(arr)
#     if(length == 1 or 0):
#         return -1
#     else:
#         num = min(arr)
#         arr.remove(num)
#         return arr
    
def solution(arr):
    minNum = min(arr)
    for i in arr:
        if(minNum == i):
            arr.remove(i)
    if(len(arr) == 0):
        return -1
    else:
        return arr

print(solution([4,3,2,1]))