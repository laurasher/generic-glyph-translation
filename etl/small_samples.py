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
# save_path = "../web/static/csv/drawn_lines/"
save_path = "../web/static/csv/drawn_marks/"

for file in fileList:
    # print(f"-- {file}")
    img_file = Image.open(file)
    # img_file.show()

    # get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_grey = img_file.convert('L')
    # img_grey.save(f'{save_path}result.png')
    # img_grey.show()

    # Save Greyscale values
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape((img_grey.size[1], img_grey.size[0]))

    df = pd.DataFrame(value)
    df = df[df>84]
    df1 = df.iloc[:,:733]
    df2 = df1.stack().reset_index()
    df2.columns = ['x_val','y_val','data_channel']

    file_rootname = file.replace(".png","").replace("images/","")
    # file_rootname = 'dl'
    # for i, s in enumerate([.0001, .00009, .00008]):
    for i, s in enumerate([5, 12, 6, 12, 4, 5, 8, 3, 6, 3, 6, 6, 6, 6, 5, 4, 8, 9, 13]):
        f = f'{save_path}{file_rootname}_{i}.csv'
        print(f)
        # df2.sample(frac=s, replace=True, random_state=1).to_csv(f)
        df2.sample(n=s, replace=True).to_csv(f)