import random
import csv

# CSV importing line adapted from https://stackoverflow.com/a/26179929
countries = list(csv.reader(open("countries.csv")))
score = 0
inGame = True

print("Welcome to European City Guesser, a game created to help you get better at GeoGuessr.")
print("")

while inGame == True:
  countryNum = random.randint(0, 36)
  country = countries[countryNum][1]
  cityNum = random.randint(2, 21)
  city = countries[countryNum][cityNum]

  answer = input("In what country is " + city + "? ")

  if(answer.casefold() == country.casefold()):
    print("Correct!")
    score += 1
  else:
    print("Incorrect! The correct country was " + country + ". Your score was " + repr(score) + ".")
    again = input("Would you like to play again? ")
    
    if again.casefold() == "yes":
      score = 0
      inGame = True
    else:
      inGame = False