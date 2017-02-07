#!/usr/bin/env python3

import sys
from random import randint

class DieModule:
  def __init__(self):
    self.RandBetween = randint

  def CreateDie(self, n):
    class D:
      def __init__(self, RandBetween):
        self.RandBetween = RandBetween

      def __call__(self, k = 1):
        return sum(self.RandBetween(1,n) for i in range(k))

      def __mul__(self, a):
        return lambda: self(a)

      def __rmul__(self, a):
        return lambda: self(a)

    return D(self.RandBetween)

  def Constant(self, n):
    return lambda: n

  def __getattr__(self, name):
    if name == '__path__':
      return ''
    try:
      return self.CreateDie(int(name[1:]))
    except:
      raise ImportError("cannot import name " + name)


sys.modules[__name__] = DieModule()
