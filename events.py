class Event: 

  def __init__(self, day, name, hour, minute, afternoon): 
    self.day = day
    self.name = name
    self.hour = hour
    self.minute = minute 
    self.afternoon = afternoon
    self.noon = "PM" if afternoon else "AM"
  
  # ['event_name'] - 'day' at 'hour' : 'minute' 'noon'
  def __str__(self): 
    return "[" + self.name + "]" + "-" + self.day.__str__() + " at " + self.hour + ":" + self.minute + self.noon
  
  def get_day(self): 
    return self.day
  
  
