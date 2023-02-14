## Installation

```shell
conda create -n open-mmlab python=3.7 pytorch==1.7.0 cudatoolkit=10.1 torchvision -c pytorch -y
conda activate open-mmlab
pip install openmim
mim install mmcv-full
mim install mmdet
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
