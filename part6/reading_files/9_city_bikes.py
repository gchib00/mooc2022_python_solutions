# Write your solution here
import math

def get_station_data(filename: str):
  stations = {}
  with open(filename) as file:
    for line in file:
      line = line.split(";")
      if line[0] == "Longitude":
        continue
      stations[line[3]] = (float(line[0]), float(line[1]))
  return stations

def distance(stations: dict, station1: str, station2: str):
  long1 = stations[station1][0]
  lat1 = stations[station1][1]
  long2 = stations[station2][0]
  lat2 = stations[station2][1]
  x_km = (long1 - long2) * 55.26
  y_km = (lat1 - lat2) * 111.2
  return math.sqrt(x_km**2 + y_km**2)

def greatest_distance(stations: dict):
  longest = {
    "station1": "",
    "station2": "",
    "distance": 0
  }
  for station in stations:
    for station2 in stations:
      long1 = stations[station][0]
      lat1 = stations[station][1]
      long2 = stations[station2][0]
      lat2 = stations[station2][1]
      x_km = (long1 - long2) * 55.26
      y_km = (lat1 - lat2) * 111.2
      if longest["distance"] < math.sqrt(x_km**2 + y_km**2):
        longest = {
          "station1": station,
          "station2": station2,
          "distance": math.sqrt(x_km**2 + y_km**2)
        }
  return (longest["station1"], longest["station2"], longest["distance"])
