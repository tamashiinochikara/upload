"""
======================
@author:沈志超
@time:2022/9/23:14:46
=====================
"""
import os
import glob
import random
import shutil
from PIL import Image
import numpy as np
'''统计均值和方差'''


if __name__ == "__main__":
    train_file = glob.glob(os.path.join('train','*','*.jpg'))
    print(train_file)
    print(f'totally {len(train_file)} files for training')
    result = []
    for file in train_file:
        img = Image.open(file).convert('RGB')
        img = np.array(img).astype(np.uint8)
        img = img/255.
        result.append(img)
    print(np.shape(result))#BS H W C
    mean = np.mean(result,axis=(0,1,2))
    std = np.std(result,axis=(0,1,2))
    print(mean)
    print(std)
