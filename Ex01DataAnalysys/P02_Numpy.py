import numpy as np
'''
Numpy : 대규모 다차원 배열을 쉽게 처리 할 수 있도록 도와 주는 파이썬의 외부 모듈
기본적으로 array라는 자료형으로 사용, 행렬 개념과 비슷
'''

a = [1,2,3,4,5]
print(a)
print(type(a))
b = np.array(a)
print(b)
print(type(b))
print(a[0])
print(b[0])
print(a[0:3])
print(b[0:3])

c = np.array(a)
print(c, type(c))
print(a+c) # list + ndarray
print(c+c) # ndarray + ndarray
print(a*2)
print(c*2)
# print(a/2) list
# print(a-a) list

print(c+2)
print(c/2)
print(c-c)

# 리스트: 요소를 기준으로 인덱싱, 넘파이행렬: 위치를 기준으로 인덱싱
a = [[1,2,3], [4,5,6], [7,8,9]]
b = np.array(a)
print(b[ :,2])
print(b[1,:2])
# array[값] 값은 인덱스가 되어 해당하는 원소를 추출
# array[:] array의 모든 성분을 추출
# array[값1:값2] 인덱스 값1에서 값2 사이의 원소를 추출
# array[값1:값2]=값3 해당값에 새로운 값3를 입력
arr = np.arange(1,11)
print(arr);print(arr[9]);print(arr[:]);print(arr[1:3])
arr[5:8] = 12  # 숫자를 작은 것에서 큰순으로 넣을 것
print(arr)

# array[행, 열] : 단일차원과 달리 다차원에서는 콤마(,)를 기준으로 행과 열로 분리
# array[행 시작,행끝 : 열시작,열끝], array[행 시작:행끝 , 열시작:열끝]
a2 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]])
print(a2[2,:]) # 2행만
print(a2[2:])  # 2행부터 끝행까지
print(a2[1:3,])  # 1~2행 추출
print(a2[:,3]) # 열의 인덱스가 3인경우만 추출
print(a2[:3,]) # 열의 인덱스가 3인경우만 추출
a2[:2, 1:3]=0
print(a2)
print(a2[3,2])
