import os
from PIL import Image
from pathlib import Path
import sys
import cv2 




i1 = "image1"
i2 = "image2"

out = "ImageMerge2.jpg"

image64 = Image.open(i1+".tif")
image128 = Image.open(i2+".tif")

blank_image = Image.new("RGB", (28000, 1400))






# datapath1 = Path("F:/2023 Letter/sogDwt2")
# print(datapath1)
# i=0
# for d in datapath1.rglob("*.tif"):
    # #print(d)
    # image64 = Image.open(d)
    # blank_image.paste(image64, (i*700,0))
    # i+=1
    # #blank_image.paste(image128, (700,0))


# datapath2 = Path("F:/2023 Letter/sogDdSu(H)")
# print(datapath2)
# i=0

# for d in datapath2.rglob("*.tif"):
    # #print(d)
    # image64 = Image.open(d)
    # blank_image.paste(image64, (i*700,700))
    # i+=1
    # #blank_image.paste(image128, (700,0))



def list_files(startpath):
    levels = 0
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        #print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        if levels < level:
            levels = level
        # i=0
        # for f in files:
            # #print('{}{}'.format(subindent, f))
              
            # if f[-3:] == "avi":
                
                # # print("Frames = ")
                # # # print(root)
                # # # print(f)
                # path = str(root) +  "\\" + f
                # folder = str(root) +  "\\"
                # # #print(path)
                # # if "nc11" in f[-10:]:
                    # # nc = "nc11"
                # # elif "nc12" in f[-10:]:
                    # # nc = "nc12"
                # # elif "nc13" in f[-10:]:
                    # # nc = "nc13"
                # # elif "nc14" in f[-10:]:
                    # # nc = "nc14"
                # # else:
                    # # nc = "NOPE"
                # #r"{}".format(string)
                # i+=1
                # FrameCapture(r"{}".format(path),i, folder)
    
    print(level)



blank_image.save(out)
# datapaths = list(map(Path,args.data))
# dirs_to_process = np.array([])
# for datapath in datapaths:
    # if datapath.exists():
        # if datapath.is_dir():
            # for datafilepath in datapath.rglob('*.ptu'):
                # parentdirpath = datafilepath.resolve().parent
                # if parentdirpath not in dirs_to_process:
                    # dirs_to_process = np.append(dirs_to_process,
                                                # parentdirpath)
                                                
                                                
                                                
                                                
                                                
path = input("Where should I look for the still frames? \n")
list_files(path)