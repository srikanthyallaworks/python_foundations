#!/usr/bin/env python

"""


"""

from dataclasses import dataclass

@dataclass(frozen=True)
class Settings:
  port:int


def get_settings():
  return Settings(5000)

