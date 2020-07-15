import os
import xml.etree.cElementTree as ET


def get_size(xml_path):
    tree = ET.ElementTree(file=xml_path)
    root = tree.getroot()
    # print(root.tag, root.attrib)
    # for child in root:
    #     print(child.tag, child.attrib)
    # node_filename = root[0].text
    # print(node_filename)

    node_size = root[4]
    node_width = int(node_size[0].text)
    node_height = int(node_size[1].text)
    node_depth = int(node_size[2].text)
    # print(node_width, node_height, node_depth)

    # lenth = len(root)
    # for i in range(6, lenth):
    #     node_obj = root[i]
    #     node_name = node_obj[0].text
    #     node_bndbox = node_obj[4]
    #     node_xmin = int(node_bndbox[0].text)
    #     node_ymin = int(node_bndbox[1].text)
    #     node_xmax = int(node_bndbox[2].text)
    #     node_ymax = int(node_bndbox[3].text)
    #     print(node_name, node_xmin, node_ymin, node_xmax, node_ymax)

    return [node_width, node_height]


if __name__ == '__main__':
    label_path = r'D:\myProject\myDatasets\监狱\VOCdevkit2007\VOC2007\Annotations'
    # label_path = r'D:\myProject\myDatasets\VOCdevkit\VOC2007\Annotations'
    label_list = os.listdir(label_path)
    # label_list = label_list[:50]
    # print(label_list)
    res = []
    for label in label_list:
        xml_path = os.path.join(label_path, label)
        tem = get_size(xml_path)
        res.append(tem)
    width = [a[0] for a in res]
    heigth = [a[1] for a in res]
    print(sum(width)/len(width), sum(heigth)/len(heigth))
