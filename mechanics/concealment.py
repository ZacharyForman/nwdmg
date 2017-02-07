#!/usr/bin/env python3

from nwdmg.mechanics.die import d100

def Default(x):
  return d100() > x

def BlindFight(x):
  return Default(x) or Default(x)
