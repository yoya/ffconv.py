#! /usr/bin/env python

import argparse
import re

helpMessage = [
    "ffconv.py  # this message"
    "ffconv.py -h # help message"
]

def help():
    print("help")
    global helpMessage
    for mesg in helpMessage:
        print(mesg)

resize = lambda x:list(map(int, x.split('x')))
crop = lambda x:list(map(int, re.split("\+|x", x)))
rotate = lambda x:int(x)

# main routine

parser = argparse.ArgumentParser(description='ffmpeg wrapper command')

parser.add_argument('-resize', type=resize, help='resize image')
parser.add_argument('-crop', type=crop, help='crop image')
parser.add_argument('-rotate', type=rotate, choices=['0', '90', '180', '270'], help='rotate image')

args = parser.parse_args()

if args.resize is not None:
    print("resize", args.resize)

if args.crop is not None:
    print("crop", args.crop)

if args.rotate is not None:
    print("rotate", args.rotate)
