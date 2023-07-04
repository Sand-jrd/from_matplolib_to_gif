#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 12:31:50 2022


        Creat a gif !

@author: sand-jrd
"""

gif_name = "mygif"

# %% 1 - Preparation

""" Arrange this section as you want, to build the plot you'd like.
Load your data , do your stuff .. Evrything you will need for the plots"""

from vip_hci.fits import open_fits
import numpy as np
from vip_hci.preproc import cube_derotate, frame_rotate


model = open_fits("model")
angles = np.linspace(90,185,90)

cube = np.array([frame_rotate(model, angle) for angle in angles]) 
static = np.median(cube,axis=0)

medsub = cube_derotate(cube - static, angles)
est_rot = np.mean(medsub, axis=0)
vmax = np.max(model)
vmin = 0

# %% 1-bis- Define the length of the gif. 
 
# ! These parameters are important and will be inherited by the next scipt  ! 
nb_frame = len(cube) # length of the gif
figsize  = (5,3)     # Size of the plot
gif_name = "mygif"   # Name the gif

# %% 2 - Plot arrangment

""" Create the plot. 
The variable *val* indicate the frame number of the gif..
"""

import matplotlib.pyplot as plt

font = {'size':'6', 'color':'tab:red' }

def plot_framek(val: int) -> None:

    num = int(val) # Val need to be convert into int. 
    
    plt.subplot(1, 3, 1)
    plt.imshow(cube[num], vmax=vmax, vmin=vmin, cmap='jet'), plt.colorbar
    plt.title("Frame n°" + str(num), **font)
    plt.gca().invert_yaxis()


    plt.subplot(1, 3, 2)
    plt.imshow(static, vmax=vmax, vmin=vmin, cmap='jet')
    plt.title("Part of the disk \nthat appear static", **font)
    plt.gca().invert_yaxis()


    plt.subplot(1,  3,  3)
    plt.imshow(est_rot, vmin=vmin, cmap='jet')
    plt.title("What's left if you\n remove static component", **font)
    plt.gca().invert_yaxis()

# %% 3 - Plot arrangment

## Test if the plot is good before generating
plt.figure("Test",figsize=figsize)
plot_framek(0)
