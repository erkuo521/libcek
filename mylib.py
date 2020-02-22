	
'''This is the example module.

This module dose stuff.
'''

__all__ = ['unpackHex', 'delstrSpace', 'cut_text']
__version__ = '0.1'
__author__ = 'PEP8'

import os
import sys
import struct
import re

import numpy as np 
from matplotlib import pyplot as plt 
import tkinter as tk
from tkinter import filedialog


class Myfile:

    def __init__(self):
        self.Applicationwindow = tk.Tk()
        self.Filetypes = [('all files', '.*'), ('text files', '.txt')]
    
    def select_file(self):
        answer = filedialog.askopenfilename(parent=self.Applicationwindow,
                                            initialdir=os.getcwd(),
                                            title="Please select a file:",
                                            filetypes=self.Filetypes)
        return answer

    def select_files(self):
        answer = filedialog.askopenfilenames(parent=self.Applicationwindow,
                                            initialdir=os.getcwd(),
                                            title="Please select one or more files:",
                                            filetypes=self.Filetypes)
        return answer

    def select_path(self):
        answer = filedialog.askdirectory(parent=self.Applicationwindow,
                                        initialdir=os.getcwd(),
                                        title="Please select a folder:")
        return answer
        
        

def unpackHex(strformat, strhex):
    numberlist = struct.unpack(strformat, bytes.fromhex(strhex))  
    return numberlist 

def delstrSpace(npndarray): #去空格
    for i in npndarray:
        tempStr =""
        for j in i:
            if j != " ":
                tempStr += j
        i = tempStr
    return npndarray
def cut_text(text,lenth): #把STR按照分隔固定长度
    textArr = re.findall('.{'+str(lenth)+'}', text) 
    textArr.append(text[(len(textArr)*lenth):]) 
    return textArr 

# print(unpackHex(">h","FFF0"))



# 字符	C类型	python类型	标准尺寸
# x	填充字节	没有意义的值	
# c	char	长度为1的字节	1
# b	signed char	整型	1
# B	unsigned char	整型	1
# ？	_Bool	布尔	1
# h	short	整型	2
# H	unsigned short	整型	2
# i	int	整型	4
# I	unsigned int	整型	4
# l	long	整型	4
# L	unsigned long	整型	4
# q	long long	整型	8
# Q	unsigned long long	整型	8
# n	ssize_t	整型	
# N	size_t	整型	
# e		浮动	2
# f	float	浮动	4
# d	double	浮动	8
# s	char[]	字节	
# p	char[]	字节	
# P	void *	整型	
