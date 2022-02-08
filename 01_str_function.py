'''
외부 라이브러리(모듈) : 다른 파이썬 파일을 읽어와서 사용
내장 함수 : 모듈을 따로 읽어오지 않고 사용
'''

# chr : 유니코드에 해당하는 글자를 뽑는 함수
print(chr(65)) #A -- +32  --> a(소문자변환)
print(chr(97)) #a -- -32  --> A(대문자변환)

for i in range(65,91):
    print(chr(i), "-", chr(i+32))

# ord : 글자의 유니코드를 출력
print(ord('A'), ord('a'))
print(ord('가'), ord('각'))

# eval : 연산식을 넣으면 해당 연산식을 계산해서 결과값을 리턴하는 함수
# 외부의 연산식을 끌어올 때, 문자타입의 식을 그대로 끌어와서 계산할 수 있음
print(eval('100+200'))
print(100+200)
a=10
print(eval('a*5'))
print(eval('min(10,20,30,40)'))


print(format(1000000)) #str(1000000)
print(format(1000000, ",")) #천단위 구별
print(format(1000000, "_"))


print(str(100)+'Hello')