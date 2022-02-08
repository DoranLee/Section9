# 목록 한 건당 인덱스와 값을 튜플로 꺼냄
lst = ['서울', '대전', '대구', '부산']
for item in enumerate(lst):
    print(item)

# 목록 한 건당 인덱스와 값을 따로 꺼냄
for index, item in enumerate(lst):
    print(index, item)

print(list(range(10)))
print(list(range(0, 10)))
print(list(range(0, 10, 2)))

# len : 저장된 데이터의 개수
print(len(lst))
print(len(range(5)))
print(len([2,6,2,5,3,4,2,34]))

# 정렬
lst1=[25,653,63,42,25,2624,4,5,43]
print(sorted(lst1)) # --> 오름차순
print(sorted(lst1,reverse=False)) # --> 오름차순
print(sorted(lst1,reverse=True)) # --> 내림차순
lst2=['d','A','w','wh','ZS','Zhw']
print(sorted(lst2)) # --> 문자 : 유니코드 순

# zip : 리스트별 한개씩 튜플로 합쳐줌
lst3=[25,66,37,83,29]
lst4=['d','A','w','wh','26','sdg']
for item in zip(lst3, lst4):
    print(item)