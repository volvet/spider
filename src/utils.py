# -*- coding: utf-8 -*-
"""
Created on Sat May  1 19:38:22 2021

@author: Administrator
"""

from enum import Enum, auto

class SpiderFormat(Enum):
  ONNX = auto()
  TORCH = auto()
  TENSORFLOW = auto()
  CAFFE = auto()
  COREML = auto()
  TNN = auto()
  MNN = auto()
 
if __name__ == '__main__':
  print(SpiderFormat(1))
  print(SpiderFormat(2))
  print(SpiderFormat(3))
  print(SpiderFormat(4))
  print(SpiderFormat(5))
  print(SpiderFormat(6))
  print(SpiderFormat(7))
