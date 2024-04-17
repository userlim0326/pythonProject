import pandas as pd
data = pd.read_csv('OBS_ASOS_TIM_2020.csv', encoding='cp949')
print(data)
print(f'{"데이터 전처리":=^20}')
data = data[['지점명', '일시', '기온(°C)']]
print(data['지점명']=='서울')
is_seoul = data['지점명']=='서울'
seoul = data[is_seoul]
print(seoul, len(seoul))
is_busan = data['지점명']=='부산'
busan = data[is_busan]
print(busan, len(busan))

temp = []
for i in seoul['일시']:
  temp.append(i.split(' ')[0])
lack_seoul = []
unique_temp = set(temp)
for i in unique_temp:
  if temp.count(i) != 24:
    lack_seoul.append(i)
print(lack_seoul)

temp = []
for i in busan['일시']:
  temp.append(i.split(' ')[0])
lack_busan = []
unique_temp = set(temp)
for i in unique_temp:
  if temp.count(i) != 24:
    lack_busan.append(i)
print(lack_busan)

lack_data = list(set(lack_seoul+lack_busan))
for i in lack_data:
  seoul = seoul[seoul['일시'].str.split('').str[0] != i]
  busan = busan[busan['일시'].str.split('').str[0] != i]

print(len(seoul))
print(len(busan))

import numpy as np
time = ['0:00','1:00','2:00','3:00','4:00','5:00','6:00','7:00','8:00','9:00',
        '10:00','11:00','12:00','13:00','14:00','15:00','16:00','17:00','18:00','19:00',
        '20:00','21:00','22:00','23:00',]
zeros = np.zeros((24, 2))
df = pd.DataFrame(zeros, index=time, columns=['seoul', 'busan'])
print(df)
