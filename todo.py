class Todo: 

  def __init__(self,day,name): 
    self.day = day
    self.name = name 

   # [TODO] - 'name' before 'day'
  def __str__(self):
    return "[TODO]" + "- " + self.name + " before " + self.day.__str__()
  
  def get_day(self): 
    return self.day
