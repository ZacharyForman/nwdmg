#!/usr/bin/env python3

class ResistanceList:
  def __init__(self):
    self.resistances = dict()

  def Set(self, resistance):
    self.resistances[resistance[0]] = (resistance[1])
    return self

  def Get(self, resistance):
    return self.resistances[resistance]

  def Resolve():
    return resistances
