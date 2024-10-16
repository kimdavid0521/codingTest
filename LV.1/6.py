# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.

# 제한 사항
# str은 길이 1 이상인 문자열입니다.

# 입출력 예
#    s	    return
# "Zbcdefg"	"gfedcbZ"

# sorted(s, reverse=True)를 사용하여 문자열 s를 역순으로 정렬합니다.
# sorted() 함수는 문자열을 각 문자의 ASCII 값에 따라 정렬하며, reverse=True 옵션을 사용하면 내림차순으로 정렬합니다.
# 예를 들어, 문자열 "Zbcdefg"를 정렬하면 ['g', 'f', 'e', 'd', 'c', 'b', 'Z']와 같은 리스트가 반환됩니다.
# join() 메서드를 사용하여 정렬된 문자열 리스트를 하나의 문자열로 결합합니다.
# join() 메서드는 문자열 리스트를 결합하여 하나의 문자열로 만들어 줍니다.
# 여기서는 빈 문자열('')을 사용하여 각 문자 사이에 아무 문자도 삽입하지 않고 그냥 이어붙이도록 합니다.
# def solution(s):
#     return ''.join(sorted(s, reverse=True))

def solution(s):
    arr = sorted(s, reverse=True) #s는 문자열이기에 s.sort로 하면 안되고 sorted(s, reverse=True라고 해야됨)
    return ''.join(arr)

print(solution("Zbcdefg"))