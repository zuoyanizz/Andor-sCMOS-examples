#!/usr/bin/env python
"""
Simple script to grab an image from Andor Neo/Zyla. 
Inefficient yes.

this uses the "imgcam.exe" program that is compiled with Cmake as per the README.

consider pyAndorNeo if this method is too basic for you.
However be aware if you want high frame rate, I couldn't even get 10fps with pyAndorNeo.

Goal is to make a simple C++ program that does a kinetic series for N hours as configured
through the command line.
This is a first step.
"""
from subprocess import check_call
from scipy.ndimage import imread
import glymur

EXP_SEC = 1. #exposure
I_MIN = 100 # intensity minimum for scaling to 8 bit
I_MAX = 5000 # intensity maximum for scaling to 8 bit -- will saturate on bright aurora!

FIN = 'image.bmp'
FOUT = 'image.jpf'

cmd = ['imgcam',
       '-e',str(EXP_SEC),
       '-s',str(I_MIN),str(I_MAX),
       '-v']

check_call(cmd)

I = imread(FIN)

glymur.Jp2k(FOUT,I,cratios=[50])