# -*- coding: utf-8 -*-
"""
Created on Mon May 10 21:23:13 2021

@author: Administrator
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from utils import SpiderFormat
from spider_factory import SpiderFactory

def test_onnxspider():
  spider = SpiderFactory.create(SpiderFormat.ONNX)
  assert spider != None
  
  
def test_torchspider():
  spider = SpiderFactory.create(SpiderFormat.TORCH)
  assert spider == None


if __name__ == '__main__':
  print('Hello, test')
  test_onnxspider()
  test_torchspider()