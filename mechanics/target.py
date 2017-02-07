#!/usr/bin/env python3

from nwdmg.mechanics.immunity_list import ImmunityList
from nwdmg.mechanics.resistance_list import ResistanceList

class Target:
  def __init__(
    self,
    dex,
    wis,
    armor_skin = False,
    dodge_feat = False,
    tumble = 0,
    armor_ac = 0,
    armor_bonus_ac = 0,
    shield_ac = 0,
    shield_bonus_ac = 0,
    natural_ac = 0,
    deflection_ac = 0,
    dodge_ac = 0,
    small_size = False,
    monk_level = 0,
    rdd_level = 0,
    pm_level = 0,
    aa_level = 0,
    concealment = 0,
    epic_dodge = False,
    deflect_arrows = False,
    immunities = ImmunityList(),
    resistances = ResistanceList()
  ):
    self.dex = dex
    self.wis = wis
    self.armor_skin = armor_skin
    self.dodge_feat = dodge_feat
    self.tumble = tumble
    self.armor_ac = armor_ac
    self.armor_bonus_ac = armor_bonus_ac
    self.shield_ac = shield_ac
    self.shield_bonus_ac = shield_bonus_ac
    self.natural_ac = natural_ac
    self.deflection_ac = deflection_ac
    self.dodge_ac = dodge_ac
    self.small_size = small_size
    self.monk_level = monk_level
    self.rdd_level = rdd_level
    self.pm_level = pm_level
    self.aa_level = aa_level
    self.concealment = concealment
    self.epic_dodge = epic_dodge
    self.deflect_arrows = deflect_arrows

  def CalculateAC():
    ac = 10
    ac += self.dex
    ac += self.wis if self.armor_ac == 0 and self.shield_ac == 0 and self.monk_level > 0
    ac += 2 if self.armor_skin
    ac += 1 if self.dodge_feat
    ac += self.armor_ac
    ac += self.armor_bonus_ac
    ac += self.shield_ac
    ac += self.shield_bonus_ac
    ac += self.natural_ac
    ac += self.deflection_ac
    ac += max(20, self.dodge_ac)
    ac += 1 if self.small_size
    ac += int(self.monk_level / 5) if self.monk_level >= 5
    ac += int(1 + self.aa_level / 3) if self.aa_level > 0 and self.monk_level == 0
    ac += int(1 + self.pm_level / 4) if self.pm_level > 0
    ac += 1 if self.rdd_level >= 1
    ac += 1 if self.rdd_level >= 5
    ac += 1 if self.rdd_level >= 8
    ac += 1 if self.rdd_level >= 10
    ac += int((self.rdd_level-10) / 5) if self.rdd_level > 10
    return ac

  def GetResistances():
    return self.resistances

  def GetImmunities():
    return self.immunities


