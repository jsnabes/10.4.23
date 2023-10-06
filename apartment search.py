# Defining function to search for appartments
def apt_search1(city, max_rent, min_beds, pets_allowed):
  # Defining the city variable using user input
  city = str(input("Which city are you looking for an apartment in? "))
  # User input for max rent
  max_rent = int(input("What is the maximum budget? "))
  # user input for number of bedrooms
  min_beds = int(input("How many bedrooms do you need? "))
  # user input for pets allowed
  pets_allowed = str(input("Are you looking for a place that allows pets? y/n "))
  # bool statement
  if pets_allowed.lower == "y":
    pets_allowed = True
  else:
    pets_allowed = False
  # print results
  print(f"{pets_allowed}")
apt_search1(2, 3, 4, 5)