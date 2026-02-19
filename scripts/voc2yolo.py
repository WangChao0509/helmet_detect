import os
import xml.etree.ElementTree as ET


# 将数据集从voc格式转为yolo格式

# ====== 修改成你的路径 ======
xml_dir = r"D:\下载\archive\Annotations"          # xml文件夹
img_dir = r'D:\下载\archive\images'              # 图片文件夹
out_dir = r'D:\下载\archive\labels'        # 输出txt文件夹

classes = ["head", "helmet"]     # 改成你的类别


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    return x * dw, y * dh, w * dw, h * dh


if not os.path.exists(out_dir):
    os.makedirs(out_dir)

for xml_file in os.listdir(xml_dir):
    if not xml_file.endswith(".xml"):
        continue

    tree = ET.parse(os.path.join(xml_dir, xml_file))
    root = tree.getroot()

    size = root.find("size")
    w = int(size.find("width").text)
    h = int(size.find("height").text)

    txt_name = xml_file.replace(".xml", ".txt")
    txt_path = os.path.join(out_dir, txt_name)

    with open(txt_path, "w") as f:
        for obj in root.iter("object"):
            cls = obj.find("name").text
            if cls not in classes:
                continue
            cls_id = classes.index(cls)

            xmlbox = obj.find("bndbox")
            xmin = float(xmlbox.find("xmin").text)
            xmax = float(xmlbox.find("xmax").text)
            ymin = float(xmlbox.find("ymin").text)
            ymax = float(xmlbox.find("ymax").text)

            x, y, w_box, h_box = convert((w, h), (xmin, xmax, ymin, ymax))
            f.write(f"{cls_id} {x} {y} {w_box} {h_box}\n")

print("转换完成")
