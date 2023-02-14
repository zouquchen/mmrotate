import os
import shutil
import cv2

catogory = ['ship']  # 指定类别的名称

# 中心path
# root_path = 'D:/zqc2/2-dataset/dota1.5'
# output_path = 'D:/zqc2/2-dataset/dota1.5_ship'

# 实验室path
root_path = 'E:/graduation-project2/4-dataset/dota1.5'
output_path = 'E:/graduation-project2/4-dataset/dota1.5_ship'


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
    content = old_txt.readlines()
    new_txt.writelines(content)

    old_txt.close()
    new_txt.close()

def select(dataset_type="train", ignore_first_two_lines=True):
    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.makedirs(output_path)

    img_path = os.path.join(root_path, dataset_type, 'images')
    label_path = os.path.join(root_path, dataset_type, "labelTxt")
    output_img_path = os.path.join(output_path, dataset_type, "images")
    output_label_path = os.path.join(output_path, dataset_type, "labelTxt")

    label_list = get_file_from_root(label_path)
    for labelpath in label_list:
        f = open(labelpath, 'r')
        lines = f.readlines()
        splitlines = [x.strip().split(' ') for x in lines]  # 根据空格分割
        for i, splitline in enumerate(splitlines):
            if ignore_first_two_lines and i in [0, 1]:  # DOTA 数据集前两行对于我们来说是无用的
                continue
            category_name = splitline[8]  # 类别名称
            if category_name in catogory:
                file_name = os.path.basename(labelpath)
                basename, abbr = file_name.split(".")  # 名称
                old_img_path = os.path.join(img_path, basename + '.png')
                new_img_path = os.path.join(output_img_path, basename + '.png')



                break
        f.close()

if __name__ == '__main__':
    select()