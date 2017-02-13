#!/usr/bin/env python
#coding=utf-8
"""

Copyright (c) 2017 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

This programm is tested on kuboki base turtlebot.

"""
import os
from PIL import Image

#图片格式
def get_imlist(search_file_path, search_file_type):
    return [os.path.join(search_file_path, f) for f in os.listdir(search_file_path) if not f.endswith(search_file_type)]

#略缩图
def tumbnail(width, height):
    Image.Image.thumbnail((width, height))