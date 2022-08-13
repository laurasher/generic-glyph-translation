from PIL import Image
import numpy as np
import sys
import os
import csv
import pandas as pd

#Useful function
def createFileList(myDir, format='.png'):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList

# load the original image
fileList = createFileList('images/')
# save_path = "results/"
save_path = "../web/static/csv/"

for file in fileList:
    print(f"-- {file}")
    img_file = Image.open(file)
    # img_file.show()

    # get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_grey = img_file.convert('L')
    img_grey.save(f'{save_path}result.png')
    img_grey.save(f'{save_path}_grayscale_intermediate.png')
    # img_grey.show()

    # Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))
    # value = value.flatten()
    df = pd.DataFrame(value)
    print("\nsave raw df csv")
    df_to_save = df
    df_to_save[df_to_save==84] = 0
    df_to_save.to_csv(f"{save_path}raw_df.csv")

    df = df[df>84]
    df1 = df.stack().reset_index()
    df1.columns = ['x_val','y_val','data_channel']

    file_rootname = file.replace(".png","").replace("images/","")
    # df.to_csv(f'{save_path}img_pixels_{file_rootname}.csv')
    # df1.to_csv(f'{save_path}img_pixels_{file_rootname}_FLAT.csv')
    print(f'{save_path}img_pixels_{file_rootname}_FLAT.csv')
    # df1.head(2000).to_csv(f'{save_path}img_pixels_{file_rootname}_FLAT_SAMPLE.csv')
    # df1.sample(frac=0.0098, replace=True, random_state=1).to_csv(f'{save_path}img_pixels_{file_rootname}_FLAT_SAMPLE.csv')
    df1.sample(frac=0.002, replace=True, random_state=1).to_csv(f'{save_path}img_pixels_{file_rootname}_FLAT_SAMPLE.csv')

    # df1.sample(frac=0.0003, replace=True, random_state=1).to_csv(f'{save_path}img_pixels_{file_rootname}_FLAT_SAMPLE_1.csv')

    # df1.sample(frac=0.0002, replace=True, random_state=1).to_csv(f'{save_path}img_pixels_{file_rootname}_FLAT_SAMPLE_2.csv')
