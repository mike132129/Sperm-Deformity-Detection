# Sperm deformity detection

## Reference Github
https://github.com/eriklindernoren/PyTorch-YOLOv3

## Custom Label Preparing

`pip install -r requirements.txt`

- Put the image dataset in `./image/`
- `python3 labeling.py`
     - press enter to start labeling
     - draw object bounding box by clicking mouse
     - press `c` to re-draw
     - press `n` or `a` to assign class (you could change corresponding to your task)
     - press `s` to save the label in `./label/`
     - press `esc` to quit

<img width="200" alt="label_example" src="https://user-images.githubusercontent.com/48711966/114554847-b8d79e80-9c99-11eb-943b-2af5bcdab5d3.png">

## Training
`python3 train.py --model_def config/yolov3-custom.cfg --data_config config/custom.data --pretrained_weights weights/darknet53.conv.74`

## Detecting
`python3 detect.py --image_folder data/custom/images/ --weights_path checkpoints/yolov3_ckpt_20.pth --model_def config/yolov3-custom.cfg --class_path data/custom/classes.names`


