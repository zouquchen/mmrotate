"""
去除标签文件的前两行
"""
import os

dota_root = "E:/graduation-project2/4-dataset/dota1.5"
old_label_folder = "labelTxt"
new_label_folder = "labelTxt_new"


def modify_txt(old_path, new_path):
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


def run(data_type="train"):
    old_label_dir = os.path.join(dota_root, data_type, old_label_folder)
    new_label_dir = os.path.join(dota_root, data_type, new_label_folder)
    if not os.path.exists(new_label_dir):
        os.mkdir(new_label_dir)

    for file in os.listdir(old_label_dir):
        modify_txt(os.path.join(old_label_dir, file), (os.path.join(new_label_dir, file)))
        print(file + " Done!")


if __name__ == '__main__':
    run("train")
    run("val")
