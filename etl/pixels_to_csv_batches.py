from PIL import Image
import numpy as np
import sys
import os
import csv
import pandas as pd
import math

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


# Compute log


def logTransform(c, f):
    g = c * math.log(float(1 + f), 10)
    return g

# Apply logarithmic transformation for an image
def logTransformImage(img, outputMax=255, inputMax=255):

    c = outputMax / math.log(inputMax + 1, 10)

    # Read pixels and apply logarithmic transformation
    for i in range(0, img.size[0] - 1):
        for j in range(0, img.size[1] - 1):
            # Get pixel value at (x,y) position of the image
            f = img.getpixel((i, j))
            # Do log transformation of the pixel
            redPixel = round(logTransform(c, f[0]))
            greenPixel = round(logTransform(c, f[1]))
            bluePixel = round(logTransform(c, f[2]))

            # Modify the image with the transformed pixel values
            img.putpixel((i, j), (redPixel, greenPixel, bluePixel))
    return img

############################################################

# Load the original image
BATCHES = 5
INPUT_FILE_LIST = createFileList("long_copper/")
save_path = "long_copper/"

for file in INPUT_FILE_LIST:
    print(
        f"\n------------------------------------------------\nFILE: {file}\n------------------------------------------------"
    )
    file_base = f"{file.split('/')[0]}"
    file_root = f"{file.split('/')[1].split('.')[0]}"
    current_img_folder = os.path.join(file_base, file_root)
    print(file_root)
    if not os.path.exists(current_img_folder):
        os.makedirs(current_img_folder)
    PIL_image = Image.open(file)

    # get original image parameters...
    width, height = PIL_image.size
    format = PIL_image.format
    mode = PIL_image.mode
    # logTransformedImage = logTransformImage(PIL_image)
    print(f"-- Image format: {format}")
    print(f"-- Image mode: {mode}")

    # Make image Greyscale
    PIL_img_grey = PIL_image.convert("L")
    # PIL_img_grey = PIL_image.convert(mode="1")
    PIL_img_grey.save(f"{save_path}_grayscale_intermediate_{file_root}.png")

    # Convert grayscale image to ARRAY
    value = np.asarray(PIL_img_grey.getdata(), dtype=np.int).reshape(
        (PIL_img_grey.size[1], PIL_img_grey.size[0])
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
        _df.to_csv(
            os.path.join(current_img_folder, f"{file_root}_flattened_{ii}.csv"),
            index=False,
        )
    # for ii in range(BATCHES):
    #     print(f"batch: {ii}")
    # df1.to_csv(f'split_triptych/{file_root}_flattened.csv', index=False)
    print("\n")
