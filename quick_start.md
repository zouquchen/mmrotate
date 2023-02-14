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
conda create -n openmmlab python=3.8 pytorch==1.8.0 torchvision==0.9.0 cudatoolkit=10.2 -c pytorch -y
conda activate open-mmlab
pip install openmim
mim install mmcv-full
mim install mmdet
```

step 2. make
```shell
git clone https://github.com/open-mmlab/mmrotate.git
cd mmrotate
pip install -r requirements/build.txt
pip install -v -e .
```

```shell
pip install opencv-python
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

## Test Dota1.0


## Train Data1.5
- 运行`tools/data/dota/labelTxtModifed.py`, 修改dota数据集的标签，去除前两行没用的
- 修改`mmrotate/datasets/dota.py`, 添加DOTA1.5中多出的一个类别
- 修改`configs/_base_/datasets/dotav1.py`, 修改data_root路径，修改train和test文件路径
- 运行脚本训练

