import pandas as pd
'''
행과 열로 이루어진 데이터를 쉽게 다룰 수 있도록 도와 주는
파이썬의 데이터 분석 전용 외부 모듈
특히 대용량의 데이터를 처리하는데 편리함
'''
# 1. Pandas의 자료형
#   1)Series 자료형
#       • 인덱스와 값을 가지고 있음
#       • 별도로 인덱스, 값을 출력할 수있음
#       • 정의할 때 인덱스를 따로 정해줄 수있음
#       • 파이썬의 딕셔너리 자료형
#       • Numpy의 Array 자료형도 Series 자료형으로 만들 수있음
#       • 딕셔너리의 키가 Series의 인덱스가 됨
sr1 = pd.Series( [ 10, 20, 30, 40], index = [ '다현', '정연', '쯔위', '사나' ] )
sr2 = pd.Series( [ 50, 60, 70, 80], index = [ '다현', '정연', '쯔위', '사나' ] )
sr3 = pd.Series( [ 11, 22, 33, 44], index = [ '다현', '사나', '모모', '재남' ])
print(sr1, type(sr1))
print(sr1.index, type(sr1.index))

sr12 = sr1 + sr2
print(sr12, '\n')

sr13 = sr1 + sr3
print(sr13)

a = pd.Series([1,2,3,4])
print(a, type(a))

#   2)DataFrame 자료형
# • 행과 열로 이루어진 자료형
# • Series와 마찬가지로 파이썬의 딕셔너리 자료형 또는 Numpy의 array로도 정의할 수있음
#   (예) Series vs. DataFrame
# • Series: 인덱스, 값으로만 구성, 1차원 배열 형태의 자료 구조
# • DataFrame: 행과 열로 구성, 2차원 테이블 형태의 자료 구조