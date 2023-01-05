class Notebook: 

  def __init__(self, name): 
    self.name = name
    self.todos = []
    self.events = []
  
  def insert_todo(self,todo):
    self.todos.append(todo)
  
  def insert_event(self,event): 
    self.events.append(event)
  
  def print_events(self): 
    print("Events: ")
    for event in self.events: 
      print(event)

  def print_todos(self): 
    print("Todos: ")
    for todo in self.todos: 
      print(todo)

  def print_everything(self): 
    self.print_events()
    self.print_todos()

  def sort_todos(self): 
    # sort (key,reverse = True/False)
    self.todos.sort(key = lambda x:x.day, reverse = True)
  
  def sort_events(self): 
    # sort (key,reverse = True/False)
    self.events.sort(key = lambda x:x.day, reverse = True)
    
