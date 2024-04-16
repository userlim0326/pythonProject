'''
데이터 시각화: 데이터 분석 결과를 시각적으로 표현하고 전달하는 과정
전문지식이 없어도 누구나 쉽게 데이터를 인지하고 활용할 수 있다.
시각화는 주로 그래프를 사용
axe는 축, 회전축
'''
import matplotlib.pyplot as plt
import numpy as np

'''
figure = plt.figure()
#add_subplot([총 행의 수][총 열의 수][subplot의 인덱스(1부터 시작)])
# axes1 = figure.add_subplot(121)  # 1행 2열에서 1열
# axes2 = figure.add_subplot(122)  # 1행 2열에서 2열
axes1 = figure.add_subplot(221)  # 2행 2열에서 1열
axes2 = figure.add_subplot(222)  # 2행 2열에서 2열
axes3 = figure.add_subplot(223)  # 2행 2열에서 3열
axes4 = figure.add_subplot(224)  # 2행 2열에서 4열
plt.show()
'''

# 직선, 꺽은 그래프
'''
figure = plt.figure()
axes = figure.add_subplot()
x = [1,2,3,4]
y = [2,4,6,8]
axes.plot(x,y)

axes = figure.add_subplot(111)
x = [1,2,3,4]
y = [2,4,6,8]
x2 = [1,2,3,4]
y2 = [4,1,3,6]
axes.plot(x,y, color="red", linestyle='dashed', marker="v", label="x")
axes.plot(x2, y2, color="k", linestyle="dotted", marker="o", label="y")
axes.legend() # plot 속성의 label을 가지고 생성
axes.set_title("x and y")
axes.set_ylabel("y")
axes.set_xlabel("x")
plt.show()
'''

# 막대그래프

figure = plt.figure()
ax = figure.add_subplot(111)
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Bar graph')
bar = ax.bar(x,y, label="y", color="pink")
ax.legend()
ax.set_ylim(0,10)
# 숫자 넣는 부분
for rect in bar:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width()/2.0, height, '%.1f' % height,
             ha='center', va='top', size = 12)

plt.show()

# 복합 축(bar and plot)
'''
figure = plt.figure()
axes = figure.add_subplot(111)
axes2 = axes.twinx()

x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

x2 = [1, 2, 3, 4]
y2 = [4, 4, 3, 6]

axes.bar(x,y,color='green', label='bar')
axes2.plot(x2,y2,color='r', label='plot')

axes.legend()
axes2.legend(loc=1)
plt.show()
'''












