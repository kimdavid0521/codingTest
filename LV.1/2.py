# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# 재한사항
# s는 길이가 1 이상, 100이하인 스트링입니다.

# 입출력 예
# s	       return
# "abcde"	"c"
# "qwer"	"we"

# def solution(s):
#     center = int(len(s)/2)
#     if(len(s) % 2 == 0):
#         word = s[center-1 : center+1]   #first:end는 first부터 end이전 요소까지 구하는거임(착각 ㄴㄴ)
#     else: 
#         word = s[center]
#     return word

def solution(s):
    center = int(len(s)/2)
    if(len(s) % 2 == 0):
        word = s[center -1 : center +1]
    else:
        word = s[center]
    return word

print(solution("adfs"))
