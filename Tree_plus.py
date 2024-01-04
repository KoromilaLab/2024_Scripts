import os
from pathlib import Path
import sys
import cv2 



yo = Path("F:")



def FrameCapture(path,nc): 


    cap= cv2.VideoCapture(path)

    totalframecount= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(nc + ", " + str(totalframecount))
  
    # # Path to video file 
    # vidObj = cv2.VideoCapture(path) 
  
    # # Used as counter variable 
    # count = 0
  
    # # checks whether frames were extracted 
    # success = 1
  
    # while success: 
  
        # # vidObj object calls read 
        # # function extract frames 
        # success, image = vidObj.read() 
  
        # # Saves the frames with frame-count 
        # cv2.imwrite("frame%d.jpg" % count, image) 
  
        # count += 1
        
        
        
        
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
            if f[-3:] == "avi":
                print("Frames = ")
                # print(root)
                # print(f)
                path = str(root) +  "\\" + f
                #print(path)
                if "nc11" in f[-10:]:
                    nc = "nc11"
                elif "nc12" in f[-10:]:
                    nc = "nc12"
                elif "nc13" in f[-10:]:
                    nc = "nc13"
                elif "nc14" in f[-10:]:
                    nc = "nc14"
                else:
                    nc = "NOPE"
                #r"{}".format(string)
                FrameCapture(r"{}".format(path),nc)





path = input("Where should I look for videos? \n")
list_files(path)
          
# list_files("F:\Sog-D")
# list_files("F:\Sog-D-D Su(H)")


  
# Function to extract frames 

        
FrameCapture(r"C:\Users\Z8 G4\Desktop\Kelli\Code\FOR PARISA DEC 2023\sogDdSu(H)\nc14\DUP_MAX_MCP GFP Nup RFP_cyo; MKRS_TM# X Sog-D-D Su (H) nc13 Airyscan Processing 4.5X, 1.77s, 2_Fiji'd-1_nc14s.avi", "")