#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:31:50 2022


        Creat a gif !

@author: sand-jrd
"""
from PIL import Image
import matplotlib.pyplot as plt
from os import makedirs, remove, rmdir
from os.path import isdir


## Make sure evrything is file "create_plot_function" is correct
## You should have edit this file beforhand to make the plot you wanted. 
from create_plot_function import *

gif_name = "mygif" # Name the gif


plt.ioff()

plt.figure("TMP_GIF",figsize=(15,6))
if not isdir("./tmp/"): makedirs("./tmp/")

images = []
for num in range(nb_frame):
    plt.cla();plt.clf()
    plot_framek(num)
    plt.savefig("/tmp/noise_" + str(num) + ".png")

for num in range(nb_frame):
    images.append(Image.open("/tmp/noise_" + str(num) + ".png"))

for num in range(nb_frame):
    try: remove("/tmp/noise_" + str(num) + ".png")
    except Exception as e: print("[WARNING] Failed to delete iter .png : " + str(e))

try : rmdir("/tmp/")
except Exception as e : print("[WARNING] Failed to remove iter dir : " + str(e))

images[0].save(fp=gif_name+".gif", format='GIF',
               append_images=images, save_all=True, duration=200, loop=0)


plt.close("TMP_GIF")
plt.ion()