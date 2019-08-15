import os
import xml.etree.ElementTree as ET


def get_objs(xml_path):

    xml_root = ET.parse(xml_path).getroot()
    obj_dict = dict()
    for obj in xml_root.iter('object'):
        box = obj.find('bndbox')
        x1 = int(box.find('xmin').text)
        y1 = int(box.find('ymin').text)
        x2 = int(box.find('xmax').text)
        y2 = int(box.find('ymax').text)
        name = obj.find('name').text
        obj_dict[x1] = [x1, y1, x2, y2, name]

    objs = [obj_dict[k] for k in sorted(obj_dict.keys())]

    return objs


if __name__ == '__main__':
    label_path = r'D:\myData\date_text\val_label'
    label_list = os.listdir(label_path)
    for label in label_list:
        xml_path = os.path.join(label_path, label)
        objs = get_objs(xml_path)

        tem = [obj[-1] for obj in objs]
        s = tem[0] + 'Y' + tem[1] + 'M' + tem[2] + 'D'
        res = label[:-4] + '.jpg' + ' ' + s
        print(res)

        file = open(r'D:\myData\date_text\val_txt.txt', 'a')
        file.write(res + '\n')
        file.close()
        print('save success!')

