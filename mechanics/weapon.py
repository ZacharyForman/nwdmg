#!/usr/bin/env python3

from copy import deepcopy
from nwdmg.mechanics.die import d4, d6, d8, d12, Constant
from nwdmg.mechanics.damage_list import DamageList

class Weapon:
  def __init__(
    self,
    base_damage,
    threat_range,
    crit_multiplier,
    keen = False,
    damage_list = DamageList(),
    enhancement = 0,
    finessable = False,
    two_hander = False,
    is_bow = False,
    massive_crit = Physical(Constant(0))):
  self.threat_range = threat_range
  self.keen = keen
  self.crit_multiplier = crit_multiplier
  self.damage_list = DamageList()
  self.damage_list.Add(Physical(base_damage))
  self.enhancement = enhancement
  self.finessable = finessable
  self.two_hander = two_hander
  self.is_bow = is_bow
  self.massive_crit = massive_crit

  def AddDamage(self, dmg):
    self.damage_list.Add(dmg)
    return self

  def GetDamage(self, str):
    if two_hander:
      str = int(str * 1.5)
    damages = deepcopy(self.damage_list)
    damages.Add(str)
    return damages
