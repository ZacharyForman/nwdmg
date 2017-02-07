#!/usr/bin/env python3

from collections import defaultdict

class DamageList:
  def __init__(self):
    self.damages = defaultdict(lambda: [])

  def Add(self, damage):
    self.damages[damage[0]].append(damage[1])
    return self

  def Merge(self, other):
    for k in other.keys():
      self.damages[k].extend(other.damages[k])
    return self

  def Resolve(self):
    return {k: sum([f() for f in self.damages[k]]) for k in self.damages}
