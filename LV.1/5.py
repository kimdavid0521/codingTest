# 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다. 예를 들어 strings가 ["sun", "bed", "car"]이고 n이 1이면 각 단어의 인덱스 1의 문자 "u", "e", "a"로 strings를 정렬합니다.

# 제한 조건
# strings는 길이 1 이상, 50이하인 배열입니다.
# strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
# strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
# 모든 strings의 원소의 길이는 n보다 큽니다.
# 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.
# 입출력 예
# strings	n	return
# ["sun", "bed", "car"]	1	["car", "bed", "sun"]
# ["abce", "abcd", "cdx"]	2	["abcd", "abce", "cdx"]


# sorted(strings)를 사용하여 입력된 문자열 리스트를 사전 순으로 정렬합니다. 
# 이때, 파이썬의 sorted() 함수는 정렬된 새로운 리스트를 반환하며, 원래의 리스트는 변경되지 않습니다.
# 이후에 다시 한 번 sorted() 함수를 호출하여 정렬된 문자열 리스트를 정렬합니다. 이번에는 정렬 기준으로 lambda 함수를 사용합니다.
# key=lambda x: x[n]을 사용하여 각 문자열을 비교할 때 인덱스 n에 해당하는 문자를 기준으로 비교합니다. 
# 이렇게 함으로써, 정렬 기준을 문자열의 특정 인덱스에 있는 문자로 지정합니다.
# 마지막으로 정렬된 리스트를 반환합니다.

# def solution(strings,n):
#     return sorted(sorted(strings), key=lambda x:x[n])

def solution(strings, n):
    strings.sort(key=lambda word: word[n])
    return strings

strings = ["sun", "bed", "car"]
n = 1
print(solution(strings, n))
