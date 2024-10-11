# String형 배열 seoul의 element중 "Kim"의 위치 x를 찾아, "김서방은 x에 있다"는 String을 반환하는 함수, solution을 완성하세요. 
# seoul에 "Kim"은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# 제한 사항
# seoul은 길이 1 이상, 1000 이하인 배열입니다.
# seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# "Kim"은 반드시 seoul 안에 포함되어 있습니다.
# 입출력 예
# seoul            	return
# ["Jane", "Kim"]	"김서방은 1에 있다"

# for i, name in enumerate(seoul)::

# enumerate() 함수를 사용하여 리스트 seoul의 각 요소와 해당 요소의 인덱스를 순회합니다.
# i는 현재 요소의 인덱스를 나타내고, name은 해당 요소를 나타냅니다.
# return "김서방은 {}에 있다".format(i):

# 'Kim'을 찾았을 때, 해당 인덱스 i를 사용하여 "김서방은 {}에 있다"라는 문자열을 생성합니다.
# format() 메서드를 사용하여 {}에 인덱스 값을 삽입합니다.
# def solution(seoul):
#     for i, name in enumerate(seoul):
#         if name == 'Kim':
#             return "김서방은 {}에 있다".format(i)

 
def solution(seoul):
    count  = 0
    for i in seoul:
        if (i == "Kim"):
            return "김서방은 " + str(count) + "에 있다"
        count = count + 1
      
print(solution(["Jane", "Kim"]))