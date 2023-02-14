CONFIG_FILE="./configs/oriented_reppoints/oriented_reppoints_r50_fpn_1x_dota_le135.py"
PROJECT_DIR="E:/graduation-project2/5-code/mmrotate_dir"
WORK_DIR="/oriented_reppoints_r50_fpn_1x_dota_le135/20230214"


python tools/train.py ${CONFIG_FILE} --work-dir ${PROJECT_DIR}${WORK_DIR}

# 实验室
python tools/train.py "./configs/oriented_reppoints/oriented_reppoints_r50_fpn_1x_dota_le135.py" --work-dir "E:/graduation-project2/5-code/mmrotate_dir/oriented_reppoints_r50_fpn_1x_dota_le135/20230214"

# 中心
python tools/train.py "./configs/oriented_reppoints/oriented_reppoints_r50_fpn_1x_dota_le135.py" --work-dir "D:/zqc2/1-code/mmrotate_dir/oriented_reppoints_r50_fpn_1x_dota_le135/20230214"