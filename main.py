from day import Day
from events import Event
from notebook import Notebook 
from todo import Todo

if __name__ == '__main__': 
  print("Welcome to the calendar application")
  application_status = True

  notebook = Notebook("First Notebook")

  while (application_status): 
    ans = input("1.view everything\n2.view upcoming events\n3.view upcoming todos\n4.add an event\n5.add a todo\n6.exit: ")
    # view everything, view upcoming events, view upcoming todos, add an event, add a todo, exit
    if ans == "1": 
      notebook.sort_todos()
      notebook.sort_events()
      notebook.print_everything()
    elif ans == "2":
      notebook.sort_events()
      notebook.print_events()
    elif ans == "3": 
      notebook.sort_todos()
      notebook.print_todos()
    elif ans == "4": 
    #name, year, month, day, hour, minute, noon, 
      name = input("Name of the event: ")
      year = input("Year of the event: ")
      month = input("Month of the event: ")
      day = input("date of the event: ")
      hour = input("Hour of the event: ")
      minute = input("Minute of the event: ")
      noon = True if(input("Please enter 1 if PM and 0 if AM: ") == "1") else False

      day = Day(day,month,year)
      #day, name, hour, minute, afternoon
      event = Event(day,name,hour,minute,noon)
      notebook.insert_event(event)
    elif ans == "5": 
       #name, year, month, day
      name = input("Name of the todo: ")
      year = input("Year of the todo: ")
      month = input("Month of the todo: ")
      day = input("date of the todo: ")

      day = Day(day,month,year)
      todo = Todo(day,name)
      notebook.insert_todo(todo)
    elif ans == "6": 
      print("Thank you for using my calendar application!")
      application_status = False
    else: 
      print("Wrong input")
