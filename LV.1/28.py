# 수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 
# 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
#가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# 제한 조건
# 시험은 최대 10,000 문제로 구성되어있습니다.
# 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
# 입출력 예
# answers	return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]

# 풀이법은 패턴을 각각 만들어주어서 반복문을 돌려주었다 
# 문제의 길이가 패턴수를 넘어가지않도록 패턴의 길이로 i의 값을 나눠줌

def solution(answers):

    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    arr = []
    score1, score2, score3 = 0,0,0
    
    length = len(answers)
    
    for i in range(length):
        if (answers[i] == pattern1[i % len(pattern1)]):
            score1 = score1 + 1
        if (answers[i] == pattern2[i % len(pattern2)]):
            score2 = score2 + 1
        if (answers[i] == pattern3[i % len(pattern3)]):
            score3 = score3 + 1
    
    maxScore = max(score1, score2, score3)
    
    if(maxScore == score1):
        arr.append(1)
    if(maxScore == score2):
        arr.append(2)
    if(maxScore == score3):
        arr.append(3)
    
    return arr
        
            
    
        