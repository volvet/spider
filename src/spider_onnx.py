# -*- coding: utf-8 -*-
"""
Created on Sun May  2 20:54:30 2021

@author: Administrator
"""

from __future__ import print_function
import sys
import os
import onnx
import coremltools.converters.onnx as coreml
from spider_base import SpiderBase
from utils import SpiderFormat
import shutil
import numpy as np


def summary_onnx_valueinfoproto(value):
  format_str = '{:>20} {:>30}'
  dims = ''
  if value.type.WhichOneof('value') == 'tensor_type':
    attend = []
    for dim in value.type.tensor_type.shape.dim:
      ele = str(dim.dim_value) if dim.WhichOneof('value') == 'dim_value' else dim.dim_param
      attend.append(ele)
    dims += 'x'.join(attend)
  return format_str.format(value.name, dims)


def summary_onnx_nodeproto(node, tensors):
  format_str = '{:>20} {:>20} {:>30}'
  dims = ''
  # TODO support other op_type
  if node.op_type == 'Conv': # conv node has 3 inputs, the 2nd is weights, 3rd is bias
    if node.input[1] in tensors:
      dims = 'x'.join([str(x) for x in tensors[node.input[1]]])
  return format_str.format(node.name, node.op_type, dims)


class SpiderOnnx(SpiderBase):
  def __init__(self):
    pass

  def convert(self, config):
    print('ONNX Convert')
    module = self.load(config.src)
    if module is None:
      print('This is not a valid onnx model:', config.src)
      return
    else:
      print('Checking model:', config.src, '. Done')

    try:
      if SpiderFormat(config.dst_format) == SpiderFormat.ONNX:
        self.convert_to_onnx(module, config)
      elif SpiderFormat(config.dst_format) == SpiderFormat.TORCH:
        self.convert_to_torch(module, config)
      elif SpiderFormat(config.dst_format) == SpiderFormat.TENSORFLOW:
        self.convert_to_tensorflow(module, config)
      elif SpiderFormat(config.dst_format) == SpiderFormat.CAFFE:
        self.convert_to_caffe(module, config)
      elif SpiderFormat(config.dst_format) == SpiderFormat.COREML:
        self.convert_to_coreml(module, config)
      elif SpiderFormat(config.dst_format) == SpiderFormat.TNN:
        self.convert_to_tnn(module, config)
      elif SpiderFormat(config.dst_format) == SpiderFormat.MNN:
        self.convert_to_mnn(module, config)
    except(Exception):
      raise
    else:
      print('ONNX converting to:', config.dst,
            '. Target format:', SpiderFormat(config.dst_format).name, '. Done')

  def summary(self, config):
    print('ONNX Summary')
    module = self.load(config.src)
    if module is None:
      print('This is not a valid onnx model:', config.src)
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
    summary_string = '--------------------------------------------------------------------------' + '\n'
    for input_value in module.graph.input:
      line = summary_onnx_valueinfoproto(input_value)
      summary_string += line + '\n'
    summary_string += '==========================================================================' + '\n'

    tensors = {}
    for tensor in module.graph.initializer:
      if tensor.name is not None and tensor.name not in tensors:
        tensors[tensor.name] = tensor.dims
    for tensor in module.graph.sparse_initializer:
      if tensor.name is not None and tensor.name not in tensors:
        tensors[tensor.name] = tensor.dims
    for op_id, op in enumerate(module.graph.node):
      summary_string += summary_onnx_nodeproto(op, tensors) + '\n'
    summary_string += '==========================================================================' + '\n'

    for output_value in module.graph.output:
      line = summary_onnx_valueinfoproto(output_value)
      summary_string += line + '\n'
    summary_string += '==========================================================================' + '\n'

    total_params = 0
    for tensor in tensors.values():
      total_params += np.prod(tensor)
    summary_string += 'Total params: ' + str(total_params) + '\n'
    summary_string += '-------------------------------------------------------------------------' + '\n'
    print(summary_string)

  def convert_to_onnx(self, module, config):
    shutil.copy(config.src, config.dst)

  def convert_to_torch(self, module, config):
    raise Exception('onnx to torch is not supported')

  def convert_to_tensorflow(self, module, config):
    raise Exception('onnx to tensorflow is not supported')

  def convert_to_caffe(self, module, config):
    raise Exception('onnx to caffe is not supported')

  def convert_to_coreml(self, module, config):
    coremlModule = coreml.convert(module, minimum_ios_deployment_target='13')
    coremlModule.save(config.dst)

  def convert_to_tnn(self, module, config):
    raise Exception('onnx to tnn is not supported')

  def convert_to_mnn(self, module, config):
    raise Exception('onnx to mnn is not supported')


if __name__ == '__main__':
  print('Hello ONNX')
