#!/usr/bin/env python
# coding=utf-8

"""
从文件列表中读取文件转换成JPEG

Copyright (c) 2017 Xu Zhihao (Howe).  All rights reserved.

This program is free software; you can redistribute it and/or modify

This programm is tested on kuboki base turtlebot.

"""
from PIL import Image
import rospy
import os
from libs import imtools

class ImageTypeConverter():
    def __init__(self):
        self.define()
        self.convert()
        self.tumbnail(width, height)

    def define(self):
        self.root_index = raw_input('请输入文件目录： ')
        self.file_type = '.jps'

    def tumbnail(self, width, height):
        Image.Image.thumbnail((width, height))

    def convert(self):
        filelist = imtools.get_imlist(self.root_index, self.file_type)
        for name in filelist:
            conv_name = os.path.split(name)[0] + self.file_type
            if name != conv_name:
                try:
                    Image.open(name).save(conv_name)
                except IOError:
                    rospy.logerr('cannot convert' + str(name))

if __name__=='__main__':
     rospy.init_node('image_type_converter')
     try:
         rospy.loginfo( "initialization system")
         ImageTypeConverter()
         rospy.loginfo("process done and quit" )
     except rospy.ROSInterruptException:
         rospy.loginfo("node terminated.")

