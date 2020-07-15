import matplotlib.pyplot as plt


# 柱状图上添加标签
def autolabel(rects, percent):
    for i, rect in enumerate(rects):
        height = rect.get_height()
        width = rect.get_width()
        x = rect.get_x()
        plt.text(x+width/2., height*1.01, '{}%'.format(round(percent[i]*100)), ha='center')


def plot2bar(xlabel, a, b):
    x = list(range(len(a)))
    width = 0.4

    prison = plt.bar(x, a, width=width, label='监狱行人', color='r')
    for i in range(len(x)):
        x[i] += width
    voc = plt.bar(x, b, width=width, label='PASCAL VOC', tick_label=xlabel, color='b')

    prison_sum = sum(a)
    VOC_sum = sum(b)
    percent_prison = [round(item / prison_sum, 3) for item in a]
    percent_VOC = [round(item / VOC_sum, 3) for item in b]
    autolabel(prison, percent_prison)
    autolabel(voc, percent_VOC)


plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
# plt.title('目标分辨率的统计')
plt.xlabel('目标分辨率范围')
plt.ylabel('目标的数量')
area_label = ['0~1000', '1000~2000', '2000~3000', '>3000']
area_prison = [3465, 4341, 1376, 50]
area_VOC = [1632, 1313, 969, 11355]
plot2bar(area_label, area_prison, area_VOC)
plt.legend()
plt.savefig('area_%.png')
plt.show()

# plt.title('目标长宽比的统计')
plt.xlabel('目标长宽比')
plt.ylabel('目标的数量')
ratio_label = ['0~0.75', '0.75~1.5', '>1.5']
ratio_prison = [16, 162, 9054]
ratio_VOC = [3886, 5877, 5506]
plot2bar(ratio_label, ratio_prison, ratio_VOC)
plt.legend()
plt.savefig('ratio_%.png')
plt.show()

