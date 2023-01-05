class Day: 

  #magic method - initializing
  def __init__(self, day, month, year): 
    self.day = day 
    self.month = month 
    self.year = year

  #string method 
  #called when you use print() or str()
  def __str__(self):
    return self.day + "/" + self.month + "/" + self.year
  
  #defines our less than operators
  def __lt__(self, other): 
    if self.year < other.self: 
      return True
    elif self.year > other.self: 
      return False 
    else: 
      if self.month < other.self: 
        return True
      elif self.month > other.self: 
        return False
      else: 
        if self.day < other.self: 
          return True
        else: 
          return False
  
  #defines our greater than operators
  def __gt__(self,other): 
    if self.year > other.self: 
      return True
    elif self.year < other.self: 
      return False 
    else: 
      if self.month > other.self: 
        return True
      elif self.month < other.self: 
        return False
      else: 
        if self.day > other.self: 
          return True
        else: 
          return False
