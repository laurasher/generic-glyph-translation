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
BATCHES = 5
fileList = createFileList("split_triptych/")
save_path = "triptych_results/"

for file in fileList:
    print(
        f"\n------------------------------------------------\nFILE: {file}\n------------------------------------------------"
    )
    file_base = f"{file.split('/')[0]}"
    file_root = f"{file.split('/')[1].split('.')[0]}"
    current_img_folder = os.path.join(file_base, file_root)
    print(file_root)
    if not os.path.exists(current_img_folder):
        os.makedirs(current_img_folder)
    img_file = Image.open(file)

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

    df1 = df.stack().reset_index()
    df1.columns = ["x_val", "y_val", "data_channel"]

    file_rootname = file.replace(".png", "").replace("images/", "")

    df1["data_channel"] = [int(x) for x in df1["data_channel"]]
    df_batched = np.array_split(df1, BATCHES)

    for ii, _df in enumerate(df_batched):
        print(ii)
        print(_df)
        _df.to_csv(os.path.join(current_img_folder, f'{file_root}_flattened_{ii}.csv'), index=False)
    # for ii in range(BATCHES):
    #     print(f"batch: {ii}")
    # df1.to_csv(f'split_triptych/{file_root}_flattened.csv', index=False)
    print("\n")
