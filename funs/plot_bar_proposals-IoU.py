import matplotlib.pyplot as plt


def plot2bar(xlabel, a, b):
    x = list(range(len(a)))
    width = 0.4

    plt.bar(x, a, width=width, label='RPN', color='b')
    for i in range(len(x)):
        x[i] += width
    plt.bar(x, b, width=width, label='IN-RPN', tick_label=xlabel, color='r')


plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
# plt.title('目标分辨率的统计')
plt.xlabel('IoU')
plt.ylabel('proposals/image')
IoU_label = ['0.5', '0.55', '0.6', '0.65', '0.7', '0.75', '0.8', '0.85', '0.9', '0.95']
# RPN = [42, 34, 27, 17, 13, 8, 5, 4, 2, 1]
# N_RPN = [46, 38, 32, 22, 16, 12, 8, 7, 4, 3]
RPN = [43, 34, 27, 17, 11, 8, 5, 3, 1, 0]
N_RPN = [45, 37, 32, 22, 16, 12, 10, 7, 3, 2]
plot2bar(IoU_label, RPN, N_RPN)
plt.legend()
plt.savefig('proposals_N-RPN.png')
plt.show()

