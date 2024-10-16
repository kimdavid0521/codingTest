# 임개발자인 "죠르디"는 크레인 인형뽑기 기계를 모바일 게임으로 만들려고 합니다.
# "죠르디"는 게임의 재미를 높이기 위해 화면 구성과 규칙을 다음과 같이 게임 로직에 반영하려고 합니다.

# crane_game_101.png

# 게임 화면은 "1 x 1" 크기의 칸들로 이루어진 "N x N" 크기의 정사각 격자이며 위쪽에는 크레인이 있고 오른쪽에는 바구니가 있습니다. (위 그림은 "5 x 5" 크기의 예시입니다). 각 격자 칸에는 다양한 인형이 들어 있으며 인형이 없는 칸은 빈칸입니다. 모든 인형은 "1 x 1" 크기의 격자 한 칸을 차지하며 격자의 가장 아래 칸부터 차곡차곡 쌓여 있습니다. 게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있습니다. 집어 올린 인형은 바구니에 쌓이게 되는 데, 이때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 됩니다. 다음 그림은 [1번, 5번, 3번] 위치에서 순서대로 인형을 집어 올려 바구니에 담은 모습입니다.

# crane_game_102.png

# 만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다. 위 상태에서 이어서 [5번] 위치에서 인형을 집어 바구니에 쌓으면 같은 모양 인형 두 개가 없어집니다.

# crane_game_103.gif

# 크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다. 또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다. (그림에서는 화면표시 제약으로 5칸만으로 표현하였음)

# 게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때, 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return 하도록 solution 함수를 완성해주세요.

# [제한사항]
# board 배열은 2차원 배열로 크기는 "5 x 5" 이상 "30 x 30" 이하입니다.
# board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
# 0은 빈 칸을 나타냅니다.
# 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
# moves 배열의 크기는 1 이상 1,000 이하입니다.
# moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.
# 입출력 예
# board	moves	result
# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4



def solution(board, moves):
    bucket = []
    score = 0
    
    # 1. board에서 뽑은 인형을 bucket에 추가
    for i in moves:
        for j in range(len(board) - 1, -1, -1):  # 인덱스 범위 수정
            if board[j][i - 1] != 0:  # board의 값이 0이 아닐 경우
                bucket.append(board[j][i - 1])
                board[j][i - 1] = 0  # 해당 위치를 0으로 변경
                break  # 인형을 뽑은 후 반복 종료

    # 2. bucket에서 중복된 인형 제거 및 점수 계산
    i = 0
    while i < len(bucket) - 1:
        if bucket[i] == bucket[i + 1]:  # 중복된 인형 발견
            score += 2  # 점수 증가
            bucket.pop(i)  # 현재 인형 제거
            bucket.pop(i)  # 다음 인형 제거
            # 인덱스는 감소하지 않음
        else:
            i += 1  # 중복이 아닐 경우 인덱스 증가

    return score

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))








# def solution(board, moves):
#     # //n*n배열중 n숫자 구하기
#     N = len(board)
#     # //n*n배열 초기화 해주기
#     arr = [[0]*N for _ in range(N)]
#     bucket = []
#     score = 0
    
#     # //행과 열 교체
#     board = map(list, zip(*board))
    
#     # //배열에 값 채우기
#     for i in range(N):
#         for j in range(N):
#             arr[i][j] = board[i][j]
            
#     for i in moves:
#         i = i-1
#         for j in range(N):
#             if(arr[i][j] != 0):
#                 doll = arr[i][j]
#                 arr[i][j] = 0
#                 if(bucket and bucket[-1] == doll):
                    
#                     score = score + 2
#                     bucket.pop()
#                 else:
#                     bucket.append(doll)
#                 break
#     return score
# 첫번째 풀이
# 실패 사유: 배열이 비어있는게아니라 0으로 들어가있는건데 비어있다고 판단해버림
# def solution(board, moves):
#     N = len(board)
#     //배열 초기화
#     arr = [[0] * N for _ in range(N)]
#     bucket_arr = [[0]*N]
#     score = 0
#     //배열 역순으로 뒤집기
#     board = list(map(list, zip(*board)))
    
#     //배열 넣기
#     for i in range(N):
#         for j in range(N):
#             arr[i][j] = board[i][j]
    
#     for i in moves:
#         for j in range(N):
#             if (len(arr[j][i]) != 0):
#                 arr.remove(arr[len(arr[j][i]) - 1][i])
#                 bucket_arr.append(arr[len(arr[j][i]) - 1][i])
#                 if(bucket_arr[len(bucket_arr)] == bucket_arr[len(bucket_arr) - 1]):
#                     score = score + 2
#                     bucket_arr.remove(bucket_arr[len(bucket_arr)])
#                     bucket_arr.remove(bucket_arr[len(bucket_arr) - 1])
    
#     return score