'''
    학생 점수 5개를 입력받은 후, 각 점수별 순위를 출력
    1등 - 90 / 2등 - 80 / 3등 - 70 / 3등 - 70 / 5등 - 40
'''
lst = []
while len(lst)<5:
    s=int(input('점수 입력 >'))
    if 0<=s<=100:
        lst.append(s)
    else :
        print('입력은 0~100 사이의 숫자만 입력하세요.')

lst = sorted(lst,reverse=True)

for s in lst :
    rank = 1
    for a in lst :
        if s < a :
            rank += 1
        else :
            break
    print(f'{rank}등 - {s}점')


# for idx, s in enumerate(sorted(lst,reverse=True)):
#     print(f'{idx+1}등 - {s}')