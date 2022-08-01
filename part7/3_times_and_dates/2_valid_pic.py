# Write your solution here
from datetime import datetime

def determine_century(marker: str):
  if marker == "+":
    return "1800"
  if marker == "-":
    return "1900"
  if marker == "A":
    return "2000"
  return None

def validate_date(yy, mm , dd):
  if ((yy % 4 == 0 and yy % 100 == 0) and yy % 400 != 0) and (mm == 2 and dd == 29):
    return False
  if dd > 31 or dd < 1:
    return False
  elif mm > 12 or mm < 1:
    return False
  elif datetime(yy, mm, dd) > datetime.now():
    return False
  return True

def calc_control_char(string: str):
  num = int(string)
  index = str(num / 31).split(".")[1]
  index = round(float("0." + index) * 31)
  special_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
  return special_string[index]

def is_it_valid(pic: str):
  if len(pic) > 11:
    return False
  dd = pic[0:2]
  mm = pic[2:4]
  yy = pic[4:6]
  control_char = pic[10]
  if control_char != calc_control_char(dd+mm+yy+pic[7:10]):
    return False
  century = determine_century(pic[6])
  if century == None:
    return False
  yy = century[0:2] + str(yy)
  if validate_date(int(yy), int(mm), int(dd)) == False:
    return False
  return True
