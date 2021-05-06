# -*- coding: utf-8 -*-
"""
Created on Sun May  2 20:54:30 2021

@author: Administrator
"""

from __future__ import print_function
import sys
import os
import onnx
from spider_base import SpiderBase

class SpiderOnnx(SpiderBase):
  def __init__(self):
    pass
  
  def convert(self, config):
    print('ONNX Convert')
    module = self.load(config.src)
    if module is None:
      print('This is not a valid onnx model: ', config.src)
      return
    else:
      print('Checking model: ', config.src, ', done')
    
    self.summary_internal(module)
   
  def summary(self, config):
    print('ONNX Summary')
    module = self.load(config.src)
    if module is None:
      print('This is not a valid onnx model: ', config.src)
      return
    self.summary_internal(module)
    

  def load(self, src):
    module = onnx.load(src)
    try:
      onnx.checker.check_model(module)
    except onnx.checker.ValidationError as e:
      print(e)
      return None
    else:
      return module
    
  def summary_internal(self, module):
    graph = module.graph
    for op_id, op in enumerate(graph.node):
      print(op_id, op)

    

if __name__ == '__main__':
  print('Hello ONNX')