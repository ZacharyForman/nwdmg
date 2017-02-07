#!/usr/bin/env python3

from nwdmg.mechanics.die import d20
from nwdmg.mechanics.damage import ResolveDamage
from nwdmg.mechanics.damage_types import DamageTypes

def AttackRoll(ab, ac, crit_range, confirm_bonus):
   ab_roll = d20()
   if ab_roll + ab < ac and ab_roll != 20:
      return 0
   if abs(ab_roll - 20) > crit_range:
      return 1
   confirm_roll = d20()
   if confirm_roll + ab < ac:
      return 1
   return 2

def SimulateRound(
  attacks,
  ac,
  damage,
  immunities,
  resistances,
  threat_range,
  crit_multiplier,
  confirmation_bonus,
  massive_crit,
  crit_immunity,
  concealment_check,
  concealment,
  sneak_damage,
  sneak_immunity,
  autododges):
  total_damage = 0
  for ab in attack_schedule:
    roll = AttackRoll(ab, ac, threat_range, confirm_bonus)
    if roll == 0:
      continue
    if crit_immunity:
      roll = 1
    if not concealment_check(concealment):
      continue
    if autododges > 0:
      autododges -= 1
      continue
    mult = 1
    mult = crit_multiplier if roll == 2
    damage_dealt = {i: 0 for i in DamageTypes()}
    for i in range(mult):
      d = damage.Resolve()
      for k in d.keys():
        damage_dealt[i] += d[k]
    damage_dealt[1] += massive_crit.Resolve()[1]
    damage_dealt[1] += sneak_damage.Resolve()[1] if not sneak_immunity
    total_damage += ResolveDamage(damage_dealt, immunities, resistances)
  return total_damage



def SimulateRounds(attacker, target, rounds=1000):
  attack_schedule = AttackSchedule(
    attacker.preepic_bab, attacker.bonus_attacks, attacker.monk_progression
  )
  ab = attacker.CalculateAB()
  attack_schedule = [prog + ab for prog in attack_schedule]
  autododges = 0
  autododges += 1 if attacker.weapon.is_bow and target.deflect_arrows
  autododges += 1 if target.epic_dodge
  running_total = 0.0
  for i in range(rounds):
    running_total += SimulateRound(
      attacks = attack_schedule,
      damage = attacker.CalculateDamage(),
      massive_crit = attacket.CalculateMassiveCrit(),
      ac = target.CalculateAC(),
      threat_range = attacker.CalculateThreatRange(),
      crit_multiplier = attacker.CalculateCritMultiplier(),
      confirmation_bonus = attacker.CalculateConfirmationBonus(),
      concealment_check = attacker.conceal_check,
      sneak_damage = attacker.CalculateSneakDamage(),
      immunities = target.GetImmunities(),
      resistances = target.GetResistances(),
      concealment = target.concealment,
      sneak_immunity = target.sneak_immunity,
      autododges = autododges
    )
  return running_total / rounds
