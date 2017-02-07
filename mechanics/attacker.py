#!/usr/bin/env python3

from nwdmg.mechanics.die import d6, Constant
from nwdmg.mechanics.attack_schedule import AttackSchedule
from nwdmg.mechanics.concealment import BlindFight, Default
from nwdmg.mechanics.damage_types import *
from nwdmg.mechanics.damage_list import DamageList

class Attacker:
  def __init__(self,
               preepic_bab,
               bab,
               str,
               dex,
               weapon,
               small_size = False,
               finesse = False,
               WF = False,
               EWF = False,
               EP = False,
               improved_critical = False,
               wm_levels = 0,
               aa_levels = 0,
               druid_and_outside = 0,
               ranger_levels = 0,
               bane_of_enemies = False,
               favored_enemy = False,
               blind_fight = Default,
               monk_progression = False,
               WS = False,
               EWS = False,
               overwhelming_crit = False,
               devastating_crit = False,
               flanking = False,
               rogue_levels = 0,
               assassin_levels = 0,
               blackguard_levels = 0,
               sneak_attacks = False,
               bonus_sneak_die = 0):
    self.damage_list = DamageList()
    self.preepic_bab = preepic_bab
    self.bab = bab
    self.str = str
    self.weapon = weapon
    self.finesse = finesse
    self.small_size = small_size
    self.WF = WF
    self.EWF = EWF
    self.EP = EP
    self.improved_critical = improved_critical
    self.wm_levels = wm_levels
    self.aa_levels = aa_levels
    self.druid_and_outside = druid_and_outside
    self.ranger_levels = ranger_levels
    self.bane_of_enemies = bane_of_enemies
    self.favored_enemy = favored_enemy
    self.conceal_check = blind_fight
    self.monk_progression = monk_progression
    self.WS = WS
    self.EWS = EWS
    self.flanking = flanking
    self.rogue_levels = rogue_levels
    self.assassin_levels = assassin_levels
    self.blackguard_levels = blackguard_levels
    self.bonus_attacks = 0
    self.bonus_ab = 0
    self.bonus_sneak_die = bonus_sneak_die

  def CalculateAB(self):
    ab = self.bab + max(self.bonus_ab + self.weapon.enhancement, 20)
    ab += self.dex if self.finesse and self.weapon.finessable else self.str
    ab += 1 if self.WF
    ab += 2 if self.EWF
    ab += 1 if self.EP
    ab += int((self.aa_levels+1)/2) if self.weapon.is_bow
    ab += 1 if self.wm_levels > 5 and self.wm_levels < 13
    ab += 1 + int((self.wm_levels-10)/3) if self.wm_levels >= 13
    ab += 2 if self.druid_and_outside
    ab += 2 if self.bane_of_enemies and self.favored_enemy
    ab += 2 if self.flanking
    ab += 1 if self.small_size
    return ab

  def CalculateSneakDie(self):
    if not self.flanking or not self.sneak_attacks:
      return Physical(Constant(0))
    sneak_die = int((self.rogue_levels+1)/2)
    sneak_die += int((self.assassin_levels+1)/2)
    sneak_die += int((self.blackguard_levels - 1) / 3)
    sneak_die += self.bonus_sneak_die
    return DamageList().Add(Physical(sneak_die * d6))

  def GetWeaponDamage(self):
    return self.weapon.GetDamage()

  def CalculateThreatRange(self):
    threat_range = self.weapon.threat_range
    threat_range *= threat_range * 2 if self.weapon.keen
    threat_range *= 2 if improved_critical
    threat_range += 2 if self.wm_levels >= 7
    threat_range += 2 if self.overwhelming_crit
    return threat_range

  def CalculateCritMultiplier(self):
    crit_mult = self.weapon.crit_multiplier
    crit_mult += 1 if self.wm_levels >= 5
    crit_mult += 1 if self.devastating_crit
    return crit_mult

  def CalculateConfirmationBonus(self):
    return 0

  def CalculateDamage(self):
    damage = self.GetWeaponDamage()
    damage.Add(Physical(Constant(2))) if self.WS
    damage.Add(Physical(Constant(4))) if self.EWS
    damage.Add(Physical(2 * d6)) if self.bane_of_enemies and self.favored_enemy
    damage.Add(Physical(Constant(int(self.ranger_levels / 5 + 1)))) if self.favored_enemy
    damage.Add(Physical(Constant(int((self.aa_levels+1)/2)))) if self.weapon.is_bow
    return damage

  def CalculateMassiveCrit(self):
    damage = DamageList()
    damage.Add(Physical(self.weapon.crit_mult * d6)) if self.overwhelming_crit
    damage.Add(self.weapon.massive_crit)
    return damage
