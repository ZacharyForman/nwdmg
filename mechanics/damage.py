#!/usr/bin/env python3

from nwdmg.mechanics.damage_types import DamageTypes

def ResolveDamage(damages, immunities, resistances):
  total_damage = 0
  for i in DamageTypes():
    total_damage += min(0, int(damages[i] * (1-immunities[i])) - resistances[i])
  return total_damage
