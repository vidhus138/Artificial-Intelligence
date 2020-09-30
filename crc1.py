# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 22:49:34 2020

@author: vidhu sharma
"""
import os
def main():
    f = open("vidhu.txt","w+")
    for i in range(10):
         f.write("This is line %d\r\n" % (i+1))
    f.close()
    f=open("vidhu.txt", "r")
    if f.mode == 'r':
       contents =f.read()
    print (contents)
    f.close()
    os.rename(r'D:\python\codes\vidhu.txt',r'D:\python\codes\vidhu1.txt')
if __name__== "__main__":
  main()