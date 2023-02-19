# BASE_PATH="D:/zqc2/1-code/mmrotate"
# PROJECT_DIR="E:/graduation-project2/5-code/mmrotate_dir"
# CONFIG_FILE="./configs/oriented_reppoints/oriented_reppoints_r50_fpn_1x_dota_le135.py"
# WORK_DIR="/oriented_reppoints_r50_fpn_1x_dota_le135/20230219"
# python tools/train.py ${CONFIG_FILE} --work-dir ${PROJECT_DIR}${WORK_DIR}

# 生成split图片
# python tools/data/dota/split/img_split.py --base-json "tools/data/dota/split/split_configs/ss_train.json"
# python tools/data/dota/split/img_split.py --base-json "tools/data/dota/split/split_configs/ss_val.json"
# python tools/data/dota/split/img_split.py --base-json "tools/data/dota/split/split_configs/ss_test.json"

# 训练
# 临时设置GPU
set CUDA_VISIBLE_DEVICES=1

# oriented_reppoints_r50
# python tools/train.py "./configs/oriented_reppoints/oriented_reppoints_r50_fpn_1x_dota_le135.py" --work-dir "D:/zqc2/1-code/mmrotate_dir/oriented_reppoints_r50_fpn_1x_dota_le135/20230217"

# rotated_reppoints
python tools/train.py "./configs/rotated_reppoints/rotated_reppoints_r50_fpn_1x_dota_le135.py" --work-dir "D:/zqc2/1-code/mmrotate_dir/rotated_reppoints_r50_fpn_1x_dota_le135/20230219"

