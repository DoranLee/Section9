# 절대값 abs
print(abs(10), abs(-10))

# 몫, 나머지 divmod --> 결과는 튜플(몫, 나머지)
print(divmod(10,7))

# 문자열 -> 정수 int
print(int('100')*2)
# 문자열 -> 실수 float
print(float('3.1415')*3)

lst = [125,4563,253,85,243,65,4,1]
# 최대값 max
print(max(lst), max(36,2,2,5,5,3235,26,4324,53))
# 최소값 min
print(min(lst), min(234.23,23523,23,22,245,523))

# 거듭제곱 pow
print(pow(2,10)) #2의 10승
print(pow(2,-3))

# 반올림 round
# …(-4)(-3)(-2)(-1).(0)(1)(2)(3)… --> 해당 자리에서 반올림하겠다.
print(round(156263.452637,4))  # 소수 n째자리까지 표기
print(round(156263.452637,-2)) # n : 0의 개수

# 총합 sum
lst1=[235,23,2,6,57,43,23623,235,4]
lst2=['h','e','l','l','o']
print(sum(lst1))
# print(sum(lst2)) --> 숫자 이외의 값은 Error