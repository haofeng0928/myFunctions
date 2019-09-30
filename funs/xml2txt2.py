import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join

classes = ["criminal", "everyman", "police"]  # 改为自己要测的目标类别


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_id):
    in_file = open('/home/fh/myProject/myData/VOCdevkit/VOC2018/Annotations/%s.xml' % (image_id))  # xml文件路径
    out_file = open('/home/fh/myProject/myData/VOCdevkit/VOC2018/yolo_label/%s.txt' % (image_id), 'w')  # txt文件保存路径
    tree = ET.parse(in_file)  # 解析xml文件
    root = tree.getroot()  # 获取xml文件的根节点
    size = root.find('size')  # 获取指定节点“图像尺寸”
    w = int(size.find('width').text)  # 获取图像宽
    h = int(size.find('height').text)  # 图像高

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text  # xml里的difficult参数
        cls = obj.find('name').text  # 要检测的类别名称
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


# VOC数据集，将VOCdevkit/VOC2007/ImageSets/Main/文件夹下所有txt循环读入
# 这里只读待训练图像的路径list.txt
image_paths = open('/home/fh/myProject/myData/VOCdevkit/VOC2018/ImageSets/Main/trainval.txt').read().strip().split()
# list_file = open('train.txt', 'w')
for image_path in image_paths:
    # list_file.write('/root/darknet-master/data/obj/%s.jpg\n'%(image_id))
    image_id = os.path.split(image_path)[1]  # image_id内容类似'0001.jpg'
    image_id2 = os.path.splitext(image_id)[0]  # image_id2内容类似'0001'
    convert_annotation(image_id2)

