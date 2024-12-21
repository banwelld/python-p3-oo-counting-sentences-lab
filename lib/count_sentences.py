#!/usr/bin/env python3

class MyString:
  def __init__(self, value: str = ""):
    self.value = value
    
  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
      
  def is_sentence(self):
    return True if self._value[-1] == "." else False
  
  def is_question(self):
    return True if self._value[-1] == "?" else False
  
  def is_exclamation(self):
    return True if self._value[-1] == "!" else False

  def count_sentences(self):
    stop_shouting = self._value.replace("!", ".")
    stop_asking = stop_shouting.replace("?", ".")
    sentences = stop_asking.split(".")
    
    sentence_count = 0
    
    for sentence in sentences:
      if sentence:
        sentence_count += 1
      
    return sentence_count
