#%%
print(2)
#%%
import shutil
import os, sys, random
from glob import glob
import pandas as pd
from shutil import copyfile
import pandas as pd
from sklearn import preprocessing, model_selection
import matplotlib.pyplot as plt
from matplotlib import patches
import numpy as np
import os

# train
python yolov5/train.py --img 640 --batch 16 --epochs 300 --data yolo_poc/tobacco_data.yaml --cfg yolov5/models/yolov5x.yaml --name Tobacco-run

#%%
# predict folder
python yolov5/detect.py --source yolov5/tobacco_yolo_format/images/valid/ --weights 'yolov5/runs/train/Tobacco-run/weights/best.pt' --hide-labels --hide-conf --classes 1 --line-thickness 2
#%%
# predict file
python yolov5/detect.py --source yolov5/tobacco_yolo_format/images/lithia/img1.jpg --weights 'yolov5/runs/train/Tobacco-run/weights/best.pt' --hide-labels --hide-conf --classes 1 --line-thickness 2