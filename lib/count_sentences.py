#!/usr/bin/env python3
import re

class MyString:
  def __init__ (self, value=""):
    self.value = value
  
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if type(value) is str:
      self._value = value
    else:
      print("The value must be a string.")
  
  def is_sentence(self):
    print(self)
    if self.value[-1] == ".":
      return True
    else:
      return False
    
  def is_question(self):
    if self.value[-1] == "?":
      return True
    else:
      return False
    
  def is_exclamation(self):
    if self.value[-1] == "!":
      return True
    else:
      return False
  
  def count_sentences(self):
    x = re.split("[.!?]", self.value)
    w = []
    for y in x:
      if y != '':
        w.append(y)
      else:
        None
    return len(w)

