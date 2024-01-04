import os
from pathlib import Path

yo = Path("F:")

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
            
list_files("F:\Sog-D")
list_files("F:\Sog-D-D Su(H)")

import cv2 
  
# Function to extract frames 
def FrameCapture(path): 


    cap= cv2.VideoCapture(path)

    totalframecount= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    print(totalframecount)
  
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
        
FrameCapture("C:\\Users\\Z8 G4\\Desktop\\Kelli\\Code\\sogDdSu(H).avi")