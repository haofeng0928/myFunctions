import matplotlib.pyplot as plt

# recall_RPN = [0.986, 0.986, 0.983, 0.979, 0.970, 0.954, 0.933]
# recall_NRPN = [0.999, 0.998, 0.997, 0.996, 0.988, 0.983, 0.971]
# x = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
recall_RPN = [0.970, 0.965, 0.958, 0.948, 0.933, 0.911, 0.874]
recall_NRPN = [0.993, 0.990, 0.986, 0.978, 0.975, 0.963, 0.936]
x = [0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8]

data = ['RPN', 'N-RPN']
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
# plt.rcParams['savefig.dpi'] = 300  # 图片像素
# plt.rcParams['figure.dpi'] = 300  # 分辨率
# plt.style.use('bmh')  # ggplot
# plt.figure(figsize=(10, 5))
# plt.title('不同backbone下FPS')
plt.xlabel("IoU")
plt.ylabel("Recall")
plt.plot(x, recall_RPN, '-o', linestyle='-', markersize=5, color='blue', label=data[0])
plt.plot(x, recall_NRPN, '-o', linestyle='-', markersize=5, color='red', label=data[1])

# plt.xlim(0, 21)
plt.ylim(0.86, 1)
plt.legend(loc=1)
plt.grid(True, linestyle='--')
plt.savefig('plot_recall_RPN.png')
plt.show()

