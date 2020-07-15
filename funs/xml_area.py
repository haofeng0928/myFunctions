import os
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt


def get_objs(xml_path):

    xml_root = ET.parse(xml_path).getroot()
    ans = []
    for obj in xml_root.iter('object'):
        box = obj.find('bndbox')
        x1 = int(box.find('xmin').text)
        y1 = int(box.find('ymin').text)
        x2 = int(box.find('xmax').text)
        y2 = int(box.find('ymax').text)
        name = obj.find('name').text
        length = y2 - y1
        width = x2 - x1
        # area = length * width
        ratio = 100*length // width
        ans.append([length, width, ratio/100, name])

    return ans


if __name__ == '__main__':
    label_path = r'D:\myProject\myDatasets\监狱\VOCdevkit2007\VOC2007\Annotations'
    # label_path = r'D:\myProject\myDatasets\VOCdevkit\VOC2007\Annotations'
    label_list = os.listdir(label_path)
    label_list = label_list[:50]
    # print(label_list)
    res = []
    count = []
    for label in label_list:
        xml_path = os.path.join(label_path, label)
        tem = get_objs(xml_path)
        res += tem
        count.append(len(tem))

    # 图像的平均尺寸
    lenth = [a[0] for a in res]
    width = [a[1] for a in res]
    print(sum(lenth)/len(lenth), sum(width)/len(width))

    # # 统计平均每张图像中目标的个数
    # mean = sum(count) / len(count)
    # print(mean)

    # # 统计目标的长宽比
    # res = sorted(res, key=lambda x: x[2])
    # ratio = [a[2] for a in res]
    # index05, index10, index20 = 0, 0, 0
    # for i in range(len(ratio)):
    #     if ratio[i] < 0.75:
    #         index05 += 1
    #     elif ratio[i] < 1.5:
    #         index10 += 1
    #     else:
    #         index20 += 1
    # print(index05, index10, index20)
