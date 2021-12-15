import pendulum

def days_to_bday(birthday):
  dd = int(birthday[0:2])
  mm = int(birthday[3:5])
  yyyy = int(birthday[-4:])
  future_bday = pendulum.datetime(yyyy, mm, dd)
  today = pendulum.now()
  delta = today - future_bday
  if delta.in_days() == 0:
    print(f"It's today! Happy Birthday!")
  elif delta.in_days() <1 :
    print(f"{abs(delta.in_days())} day(s) until your next birthday!")
  else:
    print("Your birthday has passed this year, enter the next year :)")
  return abs(delta.in_days())

  
if __name__ == "__main__":
  """Run this script specifying your birthday in dd/mm/yyyy format"""
  days_to_bday(birthday="22/10/2022")