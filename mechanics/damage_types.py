#!/usr/bin/env python3

import sys
from enum import Enum

def DamageFunc(n):
  return lambda x: (n, x)

class DamageTypeModule(Enum):
  # Physical
  Physical = DamageFunc(1)
  # Elemental
  Fire = DamageFunc(2)
  Cold = DamageFunc(3)
  Sonic = DamageFunc(4)
  Electric = DamageFunc(5)
  Acid = DamageFunc(6)
  # Exotic
  Positive = DamageFunc(7)
  Negative = DamageFunc(8)
  Magical = DamageFunc(9)
  Divine = DamageFunc(10)
  # Unblockable
  SheetDamage = DamageFunc(11)

  @staticmethod
  def DamageTypes():
    return range(1, 18)


sys.modules[__name__] = DamageTypeModule
