## this program will be a command line calendar

from time import sleep, strftime


user_name = "Aidan"
calendar = {}

def welcome():
  print "Welcome to the calendar, %s!" % (user_name)
  print "Calendar is opening..."
  sleep(1)
  print "Today is: " + strftime("%A %B, %Y")
  print "The time is: " + strftime("%H:%M:%S")
  sleep (1)

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Enter A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == "V":
      if len(calendar.keys()) == 0:
        print "Calendar is empty."
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update Successful!"
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print "Invalid date."
        try_again = raw_input("Would you like to try again? Y/N: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "Event was added successfully!"
        print calendar
    elif user_choice == "D":
      if len(calendar.keys()) == 0:
        print "Calendar is empty."
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if event == calendar[date]:
            del(calendar[date])
            print "Event successfully deleted!"
            print calendar
          else:
            print "Incorrect event specified."
    elif user_choice == "X":
      start = False

    else:
      print "Invalid command entered."
      start = False

start_calendar()


