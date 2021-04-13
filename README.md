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

![](https://i.imgur.com/1zujBzM.jpg =200x)
