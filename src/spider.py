# -*- coding: utf-8 -*-
"""
Created on Sat May  1 18:26:16 2021

@author: Administrator
"""

import os
import argparse
from utils import *
from spider_base import *
from spider_factory import *


def main(config):
  spider = SpiderFactory.create(SpiderFormat(config.src_format))
  if config.op == 'cvt':
    spider.convert(config)
  elif config.op == 'sum':
    spider.summary(config)


if __name__ == '__main__':
  cur_path = os.path.split(os.path.realpath(__file__))[0]
  parser = argparse.ArgumentParser()
  parser.add_argument('--src', type=str, default=os.path.join(cur_path, '..', 'models', 'mobilenetv2-7.onnx'))
  parser.add_argument('--dst', type=str, default='')
  parser.add_argument('--src_format', type=int, default=1)
  parser.add_argument('--dst_format', type=int, default=1)
  parser.add_argument('--op', type=str, default='cvt')
  
  config = parser.parse_args()
  print(config)
  main(config)
