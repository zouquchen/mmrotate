## Installation

step 1. prepare enviroment
```shell
conda create -n open-mmlab python=3.7 pytorch==1.7.0 cudatoolkit=10.1 torchvision -c pytorch -y
conda activate open-mmlab
pip install openmim
mim install mmcv-full
mim install mmdet
```

```shell
conda create -n openmmlab python=3.8 -y
conda activate openmmlab
conda install pytorch==1.8.0 torchvision==0.9.0 torchaudio==0.8.0 cudatoolkit=11.1 -c pytorch -c conda-forge
pip install openmim
mim install mmcv-full
mim install mmdet
```

```shell
pip install opencv-python
```

step 2. make
```shell
git clone https://github.com/open-mmlab/mmrotate.git
cd mmrotate
pip install -r requirements/build.txt
pip install -v -e .
```


## Verify the installation

Step 1. We need to download config and checkpoint files.
```shell
mim download mmrotate --config oriented_rcnn_r50_fpn_1x_dota_le90 --dest .
```
Step 2. Verify the inference demo.
```shell
python demo/image_demo.py demo/demo.jpg oriented_rcnn_r50_fpn_1x_dota_le90.py oriented_rcnn_r50_fpn_1x_dota_le90-6d2b2ce0.pth --out-file result.jpg
```
You will see a new image result.jpg on your c urrent folder

## Test Dota1.5
```shell
python tools/test.py ${CONFIG_FILE} ${CHECKPOINT_FILE} [optional arguments]
```

## Train Dota1.5
Step 1. 修改dota数据集的标签，去除前两行没用的信息(skip)
运行`tools/data/dota/labelTxtModifed.py`, 

Step 2. 添加DOTA1.5中多出的一个类别(skip)
修改`mmrotate/datasets/dota.py`, 

Step 3. 修改data_root路径，修改train和test文件路径
修改`configs/_base_/datasets/dotav1.py`, 

Step 4. split dota dataset, crop the original images into 1024×1024 patches with an overlap of 200
```shell
pip install shapely
```
```shell
python tools/data/dota/split/img_split.py --base-json tools/data/dota/split/split_configs/ss_train.json
python tools/data/dota/split/img_split.py --base-json tools/data/dota/split/split_configs/ss_val.json
python tools/data/dota/split/img_split.py --base-json tools/data/dota/split/split_configs/ss_test.json
```
Step 5. 运行脚本训练
```shell
python tools/train.py "./configs/oriented_reppoints/oriented_reppoints_r50_fpn_1x_dota_le135.py" --work-dir "D:/zqc2/1-code/mmrotate_dir/oriented_reppoints_r50_fpn_1x_dota_le135/20230214"
```

## Train for ship
Step 1. 生成数据集 dota1.5_ship
Step 2. 切图片
```shell
python tools/data/dota/split/img_split.py --base-json tools/data/dota/split/split_configs_1/ss_train.json
python tools/data/dota/split/img_split.py --base-json tools/data/dota/split/split_configs_1/ss_val.json
```
Step 3. 修改`configs/_base_/datasets/dotav1.py`
Step 4. 修改`mmrotate/datasets/dota.py`
Step 5. 训练
```shell
python tools/train.py "./configs/oriented_reppoints/oriented_reppoints_r50_fpn_1x_dota_le135.py" --work-dir "D:/zqc2/1-code/mmrotate_dir/oriented_reppoints_r50_fpn_1x_dota_le135/20230214"
```