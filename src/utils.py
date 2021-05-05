# -*- coding: utf-8 -*-
"""
Created on Sat May  1 19:38:22 2021

@author: Administrator
"""

from enum import Enum

class SpiderFormat(Enum):
  ONNX = 0
  COREML = 1
  TNN = 2
  MNN = 3
 
if __name__ == '__main__':
  print(SpiderFormat.ONNX)
  print(SpiderFormat.COREML)
  print(SpiderFormat(2))
  print(SpiderFormat(3))
