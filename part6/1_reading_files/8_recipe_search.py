# Write your solution here
def populate_recipes(recipes_src):
  recipes = []
  with open(recipes_src) as file:
    lines = []
    item = {}
    for line in file:
      lines.append(line)
    for line in lines:
      if line == "\n":
        recipes.append(item)
        item = {}
        continue
      if line == lines[-1]:
        line = line.replace("\n", "")
        if "ingredients" in item.keys():
          item["ingredients"].append(line)
        else:
          item["ingredients"] = [line]
        recipes.append(item)
        item = {}
        continue
      line = line.replace("\n", "")
      if "name" not in item.keys():
        item["name"] = line
      elif "prep_time" not in item.keys():
        item["prep_time"] = line
      else:
        if "ingredients" in item.keys():
          item["ingredients"].append(line)
        else:
          item["ingredients"] = [line]
  return recipes

def search_by_name(filename: str, word: str):
  recipes = populate_recipes(filename)
  matching_recipes = []
  for recipe in recipes:
    if "name" in recipe.keys():
      if word.lower() in recipe["name"].lower():
        matching_recipes.append(recipe["name"])
  return matching_recipes

def search_by_time(filename: str, prep_time: int):
  recipes = populate_recipes(filename)
  response = []
  for recipe in recipes:
    if "prep_time" in recipe.keys():
      if int(recipe["prep_time"]) <= prep_time:
        response.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
  return response

def search_by_ingredient(filename: str, ingredient: str):
  recipes = populate_recipes(filename)
  response = []
  for recipe in recipes:
    if "ingredients" in recipe.keys():
      if ingredient in recipe["ingredients"]:
        response.append(f"{recipe['name']}, preparation time {recipe['prep_time']} min")
  return response