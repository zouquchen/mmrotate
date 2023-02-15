BASE_PATH="D:/zqc2/1-code/mmrotate"
CONFIG_FILE="./configs/oriented_reppoints/oriented_reppoints_r50_fpn_1x_dota_le135.py"
PROJECT_DIR="E:/graduation-project2/5-code/mmrotate_dir"
WORK_DIR="/oriented_reppoints_r50_fpn_1x_dota_le135/20230214"


python tools/train.py ${CONFIG_FILE} --work-dir ${PROJECT_DIR}${WORK_DIR}

# --------实验室--------
python tools/train.py "./configs/oriented_reppoints/oriented_reppoints_r50_fpn_1x_dota_le135.py" --work-dir "E:/graduation-project2/5-code/mmrotate_dir/oriented_reppoints_r50_fpn_1x_dota_le135/20230214"

# 测试 Rotated RepPoints
python tools/test.py "configs/rotated_reppoints/rotated_reppoints_r50_fpn_1x_dota_oc.py" "E:/graduation-project2/5-code/mmrotate_dir/pretrained_models/Rotated RepPoints/rotated_reppoints_r50_fpn_1x_dota_oc-d38ce217.pth" --work-dir "E:/graduation-project2/5-code/mmrotate_dir/pretrained_models/Rotated RepPoints/_r50_fpn_1x_dota_oc" --show-dir "E:/graduation-project2/5-code/mmrotate_dir/pretrained_models/Rotated RepPoints/_r50_fpn_1x_dota_oc/vis"

# --------中心--------

# 生成split图片
python tools/data/dota/split/img_split.py --base-json "tools/data/dota/split/split_configs/ss_train.json"
python tools/data/dota/split/img_split.py --base-json "tools/data/dota/split/split_configs/ss_val.json"
python tools/data/dota/split/img_split.py --base-json "tools/data/dota/split/split_configs/ss_test.json"

# 训练
python tools/train.py "./configs/oriented_reppoints/oriented_reppoints_r50_fpn_1x_dota_le135.py" --work-dir "D:/zqc2/1-code/mmrotate_dir/oriented_reppoints_r50_fpn_1x_dota_le135/20230214"