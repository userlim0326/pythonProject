'''
데이터 시각화: 데이터 분석 결과를 시각적으로 표현하고 전달하는 과정
전문지식이 없어도 누구나 쉽게 데이터를 인지하고 활용할 수 있다.
시각화는 주로 그래프를 사용
axe는 축, 회전축
'''
import matplotlib.pyplot as plt
import numpy as np

'''
x = [1, 2, 3, 4]
y = [2, 3, 4, 5]
# plt.plot(x,y);plt.show()
# plt.bar(x,y);plt.show()
'''

'''
figure = plt.figure()
#add_subplot([총 행의 수][총 열의 수][subplot의 인덱스(1부터 시작)])
# axes1 = figure.add_subplot(121)  # 1행 2열에서 1열
# axes2 = figure.add_subplot(122)  # 1행 2열에서 2열
axes1 = figure.add_subplot(221)  # 2행 2열에서 1열
axes2 = figure.add_subplot(222)  # 2행 2열에서 2열
axes3 = figure.add_subplot(223)  # 2행 2열에서 3열
axes4 = figure.add_subplot(224)  # 2행 2열에서 4열
# plt.show()
'''

figure = plt.figure()

# 직선, 꺽은 그래프
'''
axes = figure.add_subplot()
x = [1,2,3,4]
y = [2,4,6,8]
axes.plot(x,y)

axes = figure.add_subplot(111)
x = [1,2,3,4]
y = [2,4,6,8]
x2 = [1,2,3,4]
y2 = [4,1,3,6]
axes.plot(x,y, color="red", linestyle='dashed', marker="v")
axes.plot(x2, y2, color="k", linestyle="dotted", marker="o")
'''

# 막대그래프 중복 방지
axes = figure.add_subplot(111)
x = [1, 2, 3, 4]
y = [2, 4, 6, 8]

x2 = [1, 2, 3, 4]
y2 = [4, 4, 3, 6]
tmp = x+x2
np_tmp = np.array(tmp)
np_uq = np.unique(np_tmp)
print(np.sort(np_uq))
np_sort = np.sort(np_uq)
xlabel = np.arange(len(np_sort))
print(xlabel)
width = 0.35
fig, ax = plt.subplots()

rect1 = ax.bar(xlabel - width / 2, y, width, label="x")
rect2 = ax.bar(xlabel + width / 2, y2, width, label="x2")

ax.set_ylabel('x, x2')
ax.set_title('x, x2')
ax.set_xticks(x)
ax.set_xticklabels(np_uq.tolist())
ax.legend()


def autolabel(rects):
  """Attach a text label above each bar in *rects*, displaying its height."""
  for rect in rects:
    height = rect.get_height()
    ax.annotate('{}'.format(height),
                xy=(rect.get_x() + rect.get_width() / 2, height),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

autolabel(rect1)
autolabel(rect2)

fig.tight_layout()
plt.show()
