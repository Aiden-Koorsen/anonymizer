# Program for blurring faces and number plates in an image or a video
# By Aiden Koorsen
# 05/11/2023

import sys
import os

from blur import blur_video, blur_image

# Make sure of proper usage
if len(sys.argv) != 2:
	print("Error -- wrong amount of arguments\n Usage: python anonymizer.py IN_FILE")
	quit()

# Get file and determine type and handle any errors
filename = sys.argv[1]
extension = filename.split(".")[1]

if os.path.exists(filename) == False:
	print("Error -- file " + filename + " does not exist")
	exit()

if extension == "mp4":
	blur_video(filename)
elif extension == "png" or extension == "jpeg" or extension == "jpg":
	blur_image(filename)
else:
	print("Error -- Unrecognized file format please use:\n PNG, JPEG, JPG for images\nMP4 for video")
