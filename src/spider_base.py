# -*- coding: utf-8 -*-
"""
Created on Sun May  2 20:55:32 2021

@author: Administrator
"""

import abc


class SpiderBase(abc.ABC):
  @abc.abstractmethod
  def convert(self, config):
    pass

  @abc.abstractmethod
  def summary(self, config):
    pass


if __name__ == '__main__':
  print('SpiderBase')
