#!/usr/bin/env python3

def AttackSchedule(preepic_bab, bonus_attacks = 0, monk_schedule = False):
  schedule = []
  delta = 5 if not monk_schedule else 3
  bab = preepic_bab
  while bab > 0 and len(schedule) <= 6:
    schedule.append(bab)
    bab -= delta
  bab = preepic_bab
  delta = 5
  while bonus_attacks > 0:
    schedule.append(bab)
    bab -= delta
  return schedule
