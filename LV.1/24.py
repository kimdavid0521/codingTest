# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
# 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.

# 제한 조건
# 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.
# 입출력 예
# arr1	arr2	return
# [[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
# [[1],[2]]	[[3],[4]]	[[4],[6]]

# def solution(arr1, arr2):
#     count1 = len(arr1)
#     count2 = len(arr1[0])  
#     answer = [[0] * count2 for i in range(count1)]  
    
#     for i in range(count1):
#         for j in range(count2):
#             answer[i][j] = arr1[i][j] + arr2[i][j]
    
#     return answer



def solution(arr1, arr2):
    row = len(arr1[0])
    col = len(arr1)
    result = [[0] * row for _ in range(col)]
    
    if(row != len(arr2[0]) or col != len(arr2)):
        return "두 행렬은 일치하지않습니다"
    else:
        for i in range(row):
            for j in range(col):
              result[i][j] = arr1[i][j] + arr2[i][j]
    return result  

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution(arr1, arr2))
