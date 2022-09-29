from PIL import Image
import numpy as np
import sys
import os
import csv
import pandas as pd

# Useful function
def createFileList(myDir, format=".png"):
    fileList = []
    print(myDir)
    for root, dirs, files in os.walk(myDir, topdown=False):
        for name in files:
            if name.endswith(format):
                fullName = os.path.join(root, name)
                fileList.append(fullName)
    return fileList


# load the original image
# fileList = createFileList('images/')
# fileList = createFileList('triptych_images/')
fileList = createFileList("split_triptych/")
# save_path = "results/"
save_path = "triptych_results/"
# save_path = "../web/static/csv/"
print(f"filelist {fileList}")

for file in fileList:
    print(f"-- {file}")
    file_root = f"{file.split('/')[1].split('.')[0]}"
    img_file = Image.open(file)
    # img_file.show()

    # get original image parameters...
    width, height = img_file.size
    format = img_file.format
    mode = img_file.mode

    # Make image Greyscale
    img_grey = img_file.convert("L")
    img_grey.save(f"{save_path}result_{file_root}.png")
    img_grey.save(f"{save_path}_grayscale_intermediate_{file_root}.png")
    # img_grey.show()

    # Convert graysscale image to ARRAY
    value = np.asarray(img_grey.getdata(), dtype=np.int).reshape(
        (img_grey.size[1], img_grey.size[0])
    )
    # Convert array to DATAFRAME
    df = pd.DataFrame(value)
    df_to_save = df
    # df_to_save[df_to_save==84] = 0
    # df_to_save.to_csv(f"{save_path}raw_df_{file_root}.csv")

    # df = df[df>84]
    df1 = df.stack().reset_index()
    df1.columns = ["x_val", "y_val", "data_channel"]

    file_rootname = file.replace(".png", "").replace("images/", "")
    # df.to_csv(f'{save_path}img_pixels_{file_rootname}.csv')
    # df1.to_csv(f'{save_path}img_pixels_{file_rootname}_FLAT.csv')
    # print(f'{save_path}img_pixels_{file_rootname}_FLAT.csv')
    # df1.head(2000).to_csv(f'{save_path}img_pixels_{file_rootname}_FLAT_SAMPLE.csv')
    # df1.sample(frac=0.0098, replace=True, random_state=1).to_csv(f'{save_path}img_pixels_{file_rootname}_FLAT_SAMPLE.csv')
    # df1.sample(frac=0.002, replace=True, random_state=1).to_csv(f'{save_path}img_pixels_{file_rootname}_FLAT_SAMPLE.csv')

    # df1.sample(frac=0.0003, replace=True, random_state=1).to_csv(f'{save_path}img_pixels_{file_rootname}_FLAT_SAMPLE_1.csv')

    # df1.sample(frac=0.0002, replace=True, random_state=1).to_csv(f'{save_path}img_pixels_{file_rootname}_FLAT_SAMPLE_2.csv')
    df1["data_channel"] = [int(x) for x in df1["data_channel"]]
    sample_rate = 0.001
    for _sample_rate in [1, 0.9]:
        sample_rate_str = f"{_sample_rate}".replace(".", "p")
        # df1.sample(frac=_sample_rate, replace=True, random_state=1).to_csv(f'{file_root}_cicada_flattened_sample_rate_{sample_rate_str}.csv', index=False)
        df1.to_csv(f"split_triptych/{file_root}_flattened.csv", index=False)
    print("\n")
