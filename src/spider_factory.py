# -*- coding: utf-8 -*-
"""
Created on Wed May  5 14:36:19 2021

@author: Administrator
"""


from utils import SpiderFormat
from spider_onnx import SpiderOnnx

class SpiderFactory:
  @classmethod
  def create(self, format):
    if format == SpiderFormat.ONNX:
      return SpiderOnnx()