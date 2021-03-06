import matplotlib.pyplot as plt

# data for vgg, res101, fpn
all_criminal = [[0.7697, 0.8198, 0.8663, 0.8855, 0.8698, 0.8949, 0.8935, 0.8979, 0.9000, 0.8986,
                 0.8999, 0.8994, 0.8995, 0.8978, 0.8993, 0.8996, 0.8991, 0.8986, 0.8999, 0.8990],
                [0.7679, 0.8410, 0.8852, 0.8653, 0.8490, 0.8980, 0.8971, 0.9006, 0.9011, 0.8987,
                 0.8975, 0.9008, 0.8976, 0.8987, 0.8988, 0.9029, 0.8995, 0.8992, 0.9018, 0.8994],
                [0.4388, 0.8715, 0.8854, 0.8926, 0.8951, 0.9010, 0.9005, 0.8990, 0.9003, 0.8996,
                 0.9005, 0.8979, 0.8998, 0.9002, 0.8997, 0.9008, 0.9007, 0.9008, 0.9017, 0.8991],

                [0.7173, 0.8051, 0.8819, 0.8505, 0.8831, 0.8848, 0.8861, 0.8889, 0.8778, 0.8761,
                 0.8703, 0.8749, 0.8804, 0.8800, 0.8835, 0.8819, 0.8836, 0.8843, 0.8829, 0.8843]
                ]
all_everyman = [[0.8443, 0.8686, 0.8867, 0.8902, 0.8924, 0.8916, 0.8914, 0.8902, 0.8886, 0.9235,
                 0.8943, 0.8921, 0.8945, 0.8919, 0.8915, 0.9215, 0.9270, 0.8954, 0.8939, 0.8956],
                [0.8800, 0.8915, 0.8944, 0.8884, 0.9165, 0.8972, 0.8896, 0.8908, 0.8978, 0.8941,
                 0.8930, 0.9022, 0.9014, 0.9011, 0.8999, 0.9006, 0.8911, 0.8962, 0.8991, 0.8963],
                [0.8731, 0.8871, 0.8903, 0.9159, 0.8931, 0.8991, 0.8890, 0.8996, 0.8938, 0.8920,
                 0.9023, 0.9019, 0.9045, 0.8943, 0.8956, 0.9040, 0.8861, 0.8957, 0.8939, 0.8874],

                [0.8483, 0.8744, 0.8789, 0.8943, 0.8927, 0.8929, 0.8931, 0.8940, 0.8977, 0.8917,
                 0.9006, 0.8985, 0.8992, 0.8976, 0.8990, 0.8939, 0.9002, 0.9005, 0.8994, 0.8976]
                ]
all_police = [[0.9077, 0.9078, 0.9075, 0.9082, 0.9079, 0.9079, 0.9085, 0.9084, 0.9078, 0.9078,
               0.9081, 0.9082, 0.9080, 0.9081, 0.9084, 0.9081, 0.9082, 0.9083, 0.9079, 0.9082],
              [0.9077, 0.9072, 0.9075, 0.9079, 0.9075, 0.9072, 0.9082, 0.9081, 0.9069, 0.9064,
               0.9066, 0.9064, 0.9065, 0.9064, 0.9067, 0.9062, 0.9064, 0.9060, 0.9060, 0.9061],
              [0.9034, 0.9077, 0.9080, 0.9074, 0.9068, 0.9076, 0.9071, 0.9077, 0.9073, 0.9076,
               0.9072, 0.9072, 0.9074, 0.9071, 0.9074, 0.9073, 0.9071, 0.9076, 0.9071, 0.9073],

              [0.9073, 0.9079, 0.9069, 0.9080, 0.9072, 0.9081, 0.9080, 0.9085, 0.9073, 0.9083,
               0.9073, 0.9071, 0.9069, 0.9072, 0.9077, 0.9070, 0.9072, 0.9067, 0.9072, 0.9071]
              ]
all_mAP = [[0.8406, 0.8654, 0.8868, 0.8946, 0.8900, 0.8982, 0.8978, 0.8988, 0.8988, 0.9100,
            0.9007, 0.8999, 0.9007, 0.8993, 0.8997, 0.9097, 0.9114, 0.9007, 0.9006, 0.9009],
           [0.8518, 0.8799, 0.8957, 0.8872, 0.8910, 0.9008, 0.8983, 0.8998, 0.9019, 0.8997,
            0.8990, 0.9032, 0.9018, 0.9021, 0.9018, 0.9032, 0.8990, 0.9005, 0.9023, 0.9006],
           [0.7384, 0.8888, 0.8946, 0.9053, 0.8984, 0.9026, 0.8989, 0.9021, 0.9005, 0.8997,
            0.9033, 0.9023, 0.9039, 0.9006, 0.9009, 0.9040, 0.8980, 0.9014, 0.9009, 0.8979],

           [0.8243, 0.8625, 0.8892, 0.8843, 0.8943, 0.8953, 0.8958, 0.8971, 0.8943, 0.8920,
            0.8927, 0.8935, 0.8955, 0.8949, 0.8967, 0.8943, 0.8970, 0.8972, 0.8965, 0.8963]
           ]
all_test_time = [[75.98, 75.76, 75.01, 75.42, 76.12, 75.83, 75.23, 76.34, 76.69, 75.15,
                  75.01, 75.02, 75.61, 75.73, 75.31, 75.56, 75.84, 75.85, 75.66, 75.28],
                 [96.88, 100.65, 96.82, 97.31, 97.14, 97.63, 97.35, 97.34, 98.35, 97.73,
                  97.95, 98.77, 98.20, 96.99, 97.61, 97.36, 97.65, 98.47, 98.10, 97.77],
                 [95.91, 94.34, 94.94, 94.39, 94.83, 95.00, 95.72, 95.07, 96.04, 95.45,
                  94.59, 94.21, 94.69, 94.66, 94.62, 94.24, 94.55, 94.34, 94.91, 94.58],

                 [88.22, 88.17, 88.35, 89.14, 89.17, 87.71, 90.48, 87.72, 89.71, 87.96,
                  88.37, 88.23, 87.52, 89.69, 88.56, 88.23, 89.43, 88.77, 88.65, 88.81]
                 ]

data = ['vgg', 'res101', 'fpn', 'res50']

for i in range(len(all_test_time)):
    for j in range(len(all_test_time[0])):
        all_test_time[i][j] = 1153 // all_test_time[i][j]
x = range(1, 21)
plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
# plt.rcParams['savefig.dpi'] = 300  # 图片像素
# plt.rcParams['figure.dpi'] = 300  # 分辨率
# plt.style.use('bmh')  # ggplot
# plt.figure(figsize=(10, 5))
plt.title('不同backbone下FPS')
plt.xlabel("checkpoint")
plt.ylabel("FPS")
plt.plot(x, all_test_time[0], '-o', linestyle='-', markersize=5, color='blue', label=data[0])
plt.plot(x, all_test_time[1], '-o', linestyle='-', markersize=5, color='red', label=data[1])
plt.plot(x, all_test_time[2], '-o', linestyle='-', markersize=5, color='green', label=data[2])
plt.plot(x, all_test_time[3], '-o', linestyle='-', markersize=5, color='black', label=data[3])

plt.xlim(0, 21)
# plt.ylim(70, 110)
plt.legend(loc=4)
plt.grid(True, linestyle='--')
plt.savefig('backbone_FPS.png')
plt.show()

