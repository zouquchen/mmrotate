import os
import shutil
import cv2

catagory = ['ship']  # 指定类别的名称

# 中心path
root_path = 'D:/zqc2/2-dataset/dota1.5'
output_path = 'D:/zqc2/2-dataset/dota1.5_ship'

# 实验室path
# root_path = 'E:/graduation-project2/4-dataset/dota1.5'
# output_path = 'E:/graduation-project2/4-dataset/dota1.5_ship'


def get_file_from_root(path, ext=None):
    allfiles = []
    need_ext_filter = (ext is not None)
    for root, dirs, files in os.walk(path):
        for filespath in files:
            filepath = os.path.join(root, filespath)
            extension = os.path.splitext(filepath)[1][1:]
            if need_ext_filter and extension in ext:
                allfiles.append(filepath)
            elif not need_ext_filter:
                allfiles.append(filepath)
    return allfiles


def select_txt(old_path, new_path):
    """
    去除txt文件前两行
    """
    old_txt = open(old_path, mode='r')
    new_txt = open(new_path, mode='w')
    _ = old_txt.readline()
    _ = old_txt.readline()
    for content in old_txt.readlines():
        splitlines = content.split(' ') # 根据空格分割
        if splitlines[8] in catagory:
            new_txt.write(content)
    old_txt.close()
    new_txt.close()


def select(dataset_type="train", ignore_first_two_lines=True):
    img_path = os.path.join(root_path, dataset_type, 'images')
    label_path = os.path.join(root_path, dataset_type, "labelTxt")
    output_img_path = os.path.join(output_path, dataset_type, "images")
    output_label_path = os.path.join(output_path, dataset_type, "labelTxt")

    if not os.path.exists(output_img_path):
        os.makedirs(output_img_path)
    if not os.path.exists(output_label_path):
        os.makedirs(output_label_path)

    label_list = get_file_from_root(label_path)
    for labelpath in label_list:
        f = open(labelpath, 'r')
        lines = f.readlines()
        f.close()
        splitlines = [x.strip().split(' ') for x in lines]  # 根据空格分割
        for i, splitline in enumerate(splitlines):
            if ignore_first_two_lines and i in [0, 1]:  # DOTA 数据集前两行对于我们来说是无用的
                continue
            category_name = splitline[8]  # 类别名称
            if category_name in catagory:
                file_name = os.path.basename(labelpath)
                basename, abbr = file_name.split(".")  # 名称
                old_img_path = os.path.join(img_path, basename + '.png')
                new_img_path = os.path.join(output_img_path, basename + '.png')
                old_label_path = os.path.join(labelpath)
                new_label_path = os.path.join(output_label_path, file_name)
                shutil.copy(old_img_path, new_img_path)
                select_txt(old_label_path, new_label_path)
                print(file_name + " Done!")
                break


if __name__ == '__main__':
    select("train")
    select("val")