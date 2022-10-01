"""
======================
@author:沈志超
@time:2022/9/23:12:16
=====================
"""
import os
import glob
import random
import shutil
from PIL import Image


##主要问题 windows 和mac 中的路径分隔符不一样


"""对所有图片进行RGB转化，并且统一调整至一致大小，划分训练集和数据集"""


if __name__ == "__main__":
    test_split_ratio = 0.05
    desired_size = 128 #图片统一大小
    all_data = "G:\\cs\\code\\similarity\\dataset"
    output_train_dir = "G:\\cs\\code\\similarity\\train"
    output_test_dir = "G:\\cs\\code\\similarity\\test"
    dirs = glob.glob(os.path.join(all_data,"*"))
    dirs = [d for d in dirs if os.path.isdir(d)]

    print(f"Totally {len(dirs)} classes:{dirs}")#打印所有的类

    for path in dirs:
        #对每个类别单独处理


        path = path.split('\\')[-1]#只保留类别名称 去掉G:/cs/code/similarity/dataset
        #print(path)

        os.makedirs(f'train\\{path}',exist_ok=True)
        os.makedirs(f'test\\{path}',exist_ok=True)

        files = glob.glob(os.path.join(all_data,path,'*.jpg'))
        files += glob.glob(os.path.join(all_data,path,'*.JPG'))
        files += glob.glob(os.path.join(all_data,path,'*.png'))

        #print(files)
        random.shuffle(files)

        boundary = int(len(files)*test_split_ratio)#训练集和测试集的边界

        for i, file in enumerate(files):



            #print(file.split('\\')[-1].split('.')[0] + '.jpg')



            img = Image.open(file).convert('RGB')

            print(img,':::',file)
            old_size = img.size # old_size[0] is in (width,height) format

            ratio = float(desired_size)/max(old_size)

            new_size = tuple([int(x*ratio) for x in old_size])

            im = img.resize(new_size,Image.ANTIALIAS)############

            new_im = Image.new("RGB",(desired_size,desired_size))

            new_im.paste(im,((desired_size-new_size[0])//2,
                             (desired_size-new_size[1])//2))

            assert new_im.mode == 'RGB'
            if i<= boundary:
                new_im.save(os.path.join(f'{output_test_dir}\\{path}',file.split('\\')[-1].split('.')[0] + '.jpg'))#以jpg格式保存
            else:
                new_im.save(os.path.join(f'{output_train_dir}\\{path}',file.split('\\')[-1].split('.')[0] + '.jpg'))

    test_files = glob.glob(os.path.join(output_test_dir,'*','*.jpg'))
    train_files = glob.glob(os.path.join(output_train_dir,'*','*.jpg'))

    print(f'totally {len(train_files)} files for training')
    print(f'totally {len(test_files)} files for test')
